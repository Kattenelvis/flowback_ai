from celery import shared_task
from .AI_models.area import area
from .AI_models.proposal import proposals as get_proposals
from .AI_models.prediction_statement import prediction_statements as get_prediction_statements 
from .AI_models.prediction_bets import prediction_bets
from .AI_models.voter import voter
from flowback.poll.services.area import poll_area_statement_vote_update
from flowback.poll.services.proposal import poll_proposal_create
from flowback.poll.selectors.proposal import poll_proposal_list
from flowback.poll.services.prediction import poll_prediction_statement_create, poll_prediction_bet_create
from flowback.poll.selectors.prediction import poll_prediction_statement_list, poll_prediction_bet_list
from flowback.user.selectors import get_user
from flowback.poll.services.vote import poll_proposal_vote_update
from datetime import datetime
import re

@shared_task
def area_vote_task(title:str, poll_id:int, user_id:int):
    # Currently Unused
    print("DOING", title, id)

    tags = area(title, "Uncategorized,Burn")
    tags_split = tags.content.split(',')[0]

    print("LE TAG", tags, tags_split)

    # for string in tags_split:
    #     if target_string in string:

    poll_area_statement_vote_update(user_id=user_id, poll_id=poll_id, tag=2, vote=True)
    return "DONE"


@shared_task
def proposal_task(title:str, poll_id:int, user_id:int):
    print("DOING", title, id)

    proposals = get_proposals(title)
    proposals_split = proposals.content.split(',')

    print("LE TAG", proposals, proposals_split)

    poll_proposal_create(user_id=user_id, poll_id=poll_id, title=proposals_split[0], description=" ")
    return "DONE"


@shared_task
def prediction_statement_task(poll_id:int, user_id:int, end_date):

    user = get_user(user_id)
    proposals = poll_proposal_list(poll_id=poll_id, fetched_by=user)

    predictions = get_prediction_statements(proposals[0].title, end_date)
    predictions_split = predictions.content.split(';')
    print("PREDICTING", proposals, predictions, predictions_split, int(predictions_split[0][3])-1, dict(id=int(predictions_split[0][3])-1))

    segment = [dict(proposal_id=proposals[int(predictions_split[0][3])-1].id, is_true=True)]

    poll_prediction_statement_create(user=user, 
                                     poll=poll_id, 
                                     description=predictions_split[1], 
                                     end_date=datetime.strptime(predictions_split[2].strip(), '%Y-%m-%d').date(), 
                                     segments=segment
                                    )
    return "DONE"


@shared_task
def prediction_betting_task(poll_id:int, group_id:int, user_id:int):

    user = get_user(user_id)
    proposals = poll_proposal_list(poll_id=poll_id, fetched_by=user)
    predictions = poll_prediction_statement_list(group_id=group_id, fetched_by=user)

    print("AIGHT BET", proposals, predictions)
    filtered_predictions = [obj for obj in predictions if obj.poll_id == poll_id]

    generated_predictions = prediction_bets(proposals, filtered_predictions)

    print("AIGHT BET",proposals, predictions, generated_predictions, filtered_predictions)

    generated_predictions_split = generated_predictions.content.split(',')
    score = int(generated_predictions_split[0][6:8])
    if (score == 10):
        score = 100

    score /= 20

    prediction_id = extract_prediction_number(generated_predictions[0])

    poll_prediction_bet_create(user=user_id, score=score, prediction_statement_id=prediction_id)
    return "DONE"


@shared_task
def delegation_voting_task(poll_id:int, group_id:int, user_id:int):
    
    user = get_user(user_id)
    proposals = poll_proposal_list(poll_id=poll_id, fetched_by=user)
    predictions = poll_prediction_statement_list(group_id=group_id, fetched_by=user)
    prediction_bets = poll_prediction_bet_list(group_id=group_id, fetched_by=user)

    votes = voter(prediction_array=predictions, 
          prediction_bets=prediction_bets, 
          proposal_array=proposals)

    print("VOOTER", votes)

    # poll_proposal_vote_update(user_id=user_id, poll_id=poll_id, data=votes)

    return 'DONE'


def extract_prediction_number(text):
    pattern = r"prediction (\d+)"
    match = re.search(pattern, text)
    if match:
        return int(match.group(1))
    else:
        return None

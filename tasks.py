from celery import shared_task
from .AI_models.area import area
from .AI_models.proposal import proposals as get_proposals
from .AI_models.prediction_statement import prediction_statements as get_prediction_statements
from .AI_models.prediction_bets import prediction_bets
from flowback.poll.services.area import poll_area_statement_vote_update
from flowback.poll.services.proposal import poll_proposal_create
from flowback.poll.selectors.proposal import poll_proposal_list
from flowback.poll.services.prediction import poll_prediction_statement_create, poll_prediction_bet_create
from flowback.user.selectors import get_user

@shared_task
def task(title:str, poll_id:int, user_id:int):
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
def prediction_statement_task(poll_id:int, user_id:int):

    user = get_user(user_id)
    proposals = poll_proposal_list(poll_id=poll_id, fetched_by=user)

    predictions = get_prediction_statements(proposals[0].title)
    predictions_split = predictions.content.split(',')
    print("PREDICTING", proposals, predictions, predictions_split)

    segment = [dict(id=predictions_split[0].id, active=True)]

    poll_prediction_statement_create(user=user, 
                                     poll=poll_id, 
                                     description=predictions_split[0].description, 
                                     end_date=predictions_split[0].date, 
                                     segments=segment
                                    )
    return "DONE"


def parse_array_to_dict(arr):
    print("Hello?",arr)
    result = []
    for item in arr:
        parts = item.split(' at time ')
        description = parts[0].split('. ')[1]
        time = parts[1]
        pos = int(parts[0].split('. ')[0])
        result.append({'pos': pos, 'description': description, 'time': time})
    return result

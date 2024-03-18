from celery import shared_task
from .AI_models.area import area
from .AI_models.proposal import proposals
from flowback.poll.services.area import poll_area_statement_vote_update
from flowback.poll.services.proposal import poll_proposal_create


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
def proposalTask(title:str, poll_id:int, user_id:int):
    print("DOING", title, id)

    generated_proposals = proposals(title)
    proposals_split = generated_proposals.content.split(',')

    print("LE TAG", generated_proposals, proposals_split)

    poll_proposal_create(user_id=user_id, poll_id=poll_id, title=proposals_split[0], description=" ")
    return "DONE"

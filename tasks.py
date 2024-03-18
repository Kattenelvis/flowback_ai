from celery import shared_task
from .AI_models.area import area
from flowback.poll.services.area import poll_area_statement_vote_update


@shared_task
def task(title:str, poll_id:int, user_id:int):
    print("DOING", title, id)

    tag = area(title)

    print("LE TAG", tag)

    poll_area_statement_vote_update(user_id=user_id, poll_id=poll_id, tag=2, vote=True)
    return "DONE"

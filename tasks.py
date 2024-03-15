from django.dispatch import receiver
from django.db.models.signals import post_save
from django.http import HttpResponse

from flowback.poll.models import Poll
from celery import  shared_task

import requests
import json

# start_date
# area_vote_end_date
# proposal_end_date
# prediction_statement_end_date
# prediction_bet_end_date
# delegate_vote_end_date
# vote_end_date
# end_date

@receiver(post_save, sender=Poll)
def savePoll(sender, instance, *args, **kwargs):
    print("HERE at save poll")
    get_request()
    task.apply_async(eta=instance.start_date)
    return HttpResponse("DONE")


@shared_task
def task():
    post_request()
    print("DONE")
    return "DONE"


def post_request():
    url = "http://localhost:8000/group/poll/46/area/update"
    header = {
    "Content-Type":"application/json",
    }
    payload = {   
        "tag":"2",
        "vote":"true"
    }
    result = requests.post(url,  data=json.dumps(payload), headers=header)
    if result.status_code == 200:
        return HttpResponse('Successful')
    return HttpResponse('Something went wrong')

def get_request():
    url = "http://localhost:8000/group/1/poll/list"
    header = {
    "Content-Type":"application/json"
    }
    
    results = requests.get(url,headers=header)
    if results.status_code == 200:
        print("YAYY", results)
        return HttpResponse('Successful')
    print("boooo", results)
    return HttpResponse('Something went wrong')
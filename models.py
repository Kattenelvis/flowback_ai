#TODO: Put this in another file...for some reason it stops working otuside of models.py
from flowback.poll.models import Poll
from flowback.comment.models import Comment
from flowback.kanban.models import KanbanEntry

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from celery import Celery, shared_task
import environ
from time import sleep

import json
import requests
from django.http import HttpResponse

def post_request():
    print("IS NOW POSTING")
    url = "http://localhost:8000/group/poll/72/area/update"
    header = {
    "Content-Type":"application/json",
    "Authorization": "Token c0b06baef35a5068e18c8fe4d2c383bc20fc4c7d"
    }
    payload = {   
        "tag":"2",
        "vote":"true"
    }
    result = requests.post(url,  data=json.dumps(payload), headers=header)
    if result.status_code == 200:
        return HttpResponse('Successful')
    print("RESULSTS", result)
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


@receiver(post_save, sender=Poll)
def savePoll(sender, instance, *args, **kwargs):
    print("POLL UPDATE", sender, instance, args, kwargs)
    # post_request()
    task.apply_async(eta=instance.start_date)
    return HttpResponse('Successful')


@shared_task
def task():
    # sleep(5)
    print("DOING")
    post_request()
    return "DONE"

app = Celery('backend')
env = environ.Env(RABBITMQ_BROKER_URL=str)
broker_url = env('RABBITMQ_BROKER_URL')

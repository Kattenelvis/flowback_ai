from flowback.poll.models import Poll
from flowback.comment.models import Comment
from flowback.kanban.models import KanbanEntry

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from celery import Celery, shared_task
import environ
from time import sleep

@receiver(post_save, sender=Poll)
def savePoll(sender, instance, *args, **kwargs):
    print("POLL UPDATE", sender, instance, args, kwargs)
    task()


@shared_task
def task():
    sleep(5)
    print("DONE")
    return "DONE"

app = Celery('backend')
env = environ.Env(RABBITMQ_BROKER_URL=str)
broker_url = env('RABBITMQ_BROKER_URL')



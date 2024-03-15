from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from flowback.poll.models import Poll
from flowback.comment.models import Comment
from celery import  shared_task
from datetime import datetime, timedelta

@receiver(post_save, sender=Comment)
def savePoll(sender, instance, *args, **kwargs):
    print("POLL UPDATE", sender, instance, args, kwargs)

    slight_future = datetime.now() + timedelta(seconds=5)
    task.apply_async(eta=slight_future)
    return HttpResponse("DONE")


@shared_task
def task():
    


    print("DONE")
    return "DONE"



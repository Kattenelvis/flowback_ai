from django.dispatch import receiver
from django.db.models.signals import post_save
from django.http import HttpResponse

from flowback.poll.models import Poll
from celery import  shared_task


@receiver(post_save, sender=Poll)
def savePoll(sender, instance, *args, **kwargs):
    task.apply_async(eta=instance.area_vote_end_date)
    return HttpResponse("DONE")


@shared_task
def task():
    print("DONE")
    return "DONE"



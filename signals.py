from flowback.poll.models import Poll
from django.dispatch import receiver
from django.db.models.signals import post_save
from .tasks import task
from django.http import HttpResponse

@receiver(post_save, sender=Poll)
def savePoll(sender, instance, *args, **kwargs):
    print("POLL UPDATE", sender, instance, args, kwargs)
    task.apply_async(kwargs=dict(title=instance.title, poll_id=instance.id, user_id=instance.created_by.id), eta=instance.start_date)
    print("DID IT WORK?")
    return HttpResponse('Successful')

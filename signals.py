from flowback.poll.models import Poll
from django.dispatch import receiver
from django.db.models.signals import post_save
from .tasks import task, proposalTask
from django.http import HttpResponse

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
    print("POLL UPDATE", sender, instance, args, kwargs)
    proposalTask.apply_async(kwargs=dict(title=instance.title, poll_id=instance.id, user_id=instance.created_by.id), eta=instance.area_vote_end_date)
    print("DID IT WORK?")
    return HttpResponse('Successful')

from flowback.poll.models import Poll
from django.dispatch import receiver
from django.db.models.signals import post_save
from .tasks import proposal_task, prediction_statement_task, prediction_betting_task, delegation_voting_task
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
    
    proposal_task.apply_async(kwargs=dict(title=instance.title, poll_id=instance.id, user_id=instance.created_by.id), 
        eta=instance.area_vote_end_date)
    
    prediction_statement_task.apply_async(kwargs=dict(poll_id=instance.id, user_id=instance.created_by.id, end_date=instance.end_date), 
        eta=instance.proposal_end_date)
    
    prediction_betting_task.apply_async(kwargs=dict(poll_id=instance.id, user_id=instance.created_by.id, group_id=instance.created_by.group_id), 
        eta=instance.prediction_statement_end_date)
    
    delegation_voting_task.apply_async(kwargs=dict(poll_id=instance.id, user_id=instance.created_by.id, group_id=instance.created_by.group_id), 
        eta=instance.delegate_vote_end_date)
    

    print("DID IT WORK?")
    return HttpResponse('Successful')

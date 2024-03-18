from celery import shared_task
import environ
from time import sleep

import json
import requests
from django.http import HttpResponse

from .AI_models.area import area
from flowback.poll.services.area import poll_area_statement_vote_update

# def post_request(id:int, group_id:int, payload):
#     print("IS NOW POSTING")
#     url = f"http://localhost:8000/group/poll/{group_id}/area/update"
#     header = {
#     "Content-Type":"application/json",
#     "Authorization": "Token c0b06baef35a5068e18c8fe4d2c383bc20fc4c7d"
#     }
#     result = requests.post(url,  data=json.dumps(payload), headers=header)
#     if result.status_code == 200:
#         return HttpResponse('Successful')
#     print("RESULSTS", result)
#     return HttpResponse('Something went wrong')

# def get_request():
#     url = "http://localhost:8000/group/1/poll/list"
#     header = {
#     "Content-Type":"application/json"
#     }
    
#     results = requests.get(url,headers=header)
#     if results.status_code == 200:
#         print("YAYY", results)
#         return HttpResponse('Successful')
#     print("boooo", results)
#     return HttpResponse('Something went wrong')




@shared_task
def task(title:str, poll_id:int, user_id:int):
    print("DOING", title, id)

    tag = area(title)

    print("LE TAG", tag)

    # payload = {
    #     "vote":"true",
    #     "tag": "2"
    # }

    poll_area_statement_vote_update(user_id=user_id, poll_id=poll_id, tag=2, vote=True)
    # post_request(title, group_id, payload)
    return "DONE"

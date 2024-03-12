from django.urls import path
from flowback_addon.flowback_ai.views import AIViewAPI, pollTitleAPI, proposalAPI

ai_patterns = [
    path('titles', pollTitleAPI.as_view(), name="ai_poll_title"),
    path('poll', AIViewAPI.as_view(), name='ai_test_view'),
    path('proposal', proposalAPI.as_view(), name='ai_proposal'),
]
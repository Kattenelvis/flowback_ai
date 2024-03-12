from django.urls import path
from flowback_addon.flowback_ai.views import AIViewAPI, pollTitleAPI, proposalAPI, prediction_statementAPI, prediction_betsAPI

ai_patterns = [
    path('titles', pollTitleAPI.as_view(), name="ai_poll_title"),
    path('poll', AIViewAPI.as_view(), name='ai_test_view'),
    path('proposal', proposalAPI.as_view(), name='ai_proposal'),
    path('prediction_statement', prediction_statementAPI.as_view(), name='ai_prediction_statement'),
    path('prediction_bets', prediction_betsAPI.as_view(), name='ai_prediction_statement'),
]
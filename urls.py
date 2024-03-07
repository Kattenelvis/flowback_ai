from django.urls import path
from flowback_addon.flowback_ai.views import AIViewAPI, pollTitleAPI

ai_patterns = [
    path('test', AIViewAPI.as_view(), name='ai_test_view'),
    path('test/post', AIViewAPI.as_view(), name='ai_test_view'),
    path('titles', pollTitleAPI.as_view(), name="ai_poll_title")
]
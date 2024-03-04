from django.urls import path
from flowback_addon.flowback_ai.views import AIViewAPI

ai_patterns = [
    path('test', AIViewAPI.as_view(), name='ai_test_view')
]
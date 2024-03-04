Git clone this project in flowback-backend/flowback_addon

python3 -m venv venv
source venv/bin/activate
pip install openai

cd ../../
pip install openai


Seems to work for some reason, even if the second pip install 


Make sure that flowback_addon/urls.py (NOT flowback_ai/urls.py) includes the following:

from django.urls import path, include

from flowback_addon.flowback_ai.urls import ai_patterns

addon_patterns = [
     path('ai/', include((ai_patterns, 'ai')))
]

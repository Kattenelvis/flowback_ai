This project first requires that you've installed Flowback backend. A setup can be found here https://github.com/Gofven/flowback-setup-docker

Git clone this project in flowback-backend/flowback_addon

python3 -m venv venv 
Linux: source venv/bin/activate
Windows: venv\Scripts\activate
pip install openai

Make sure that flowback_addon/urls.py (NOT flowback_ai/urls.py) includes the following:

from django.urls import path, include

from flowback_addon.flowback_ai.urls import ai_patterns

addon_patterns = [
     path('ai/', include((ai_patterns, 'ai')))
]


Also ensure that the environmental variable in main flowback-backend repo is set to
INTEGRATIONS="flowback_addon.flowback_ai"
OPENAI_API_KEY=<api-key> 

Where <api-key> is your private key generated and paid for at https://platform.openai.com/api-keys

In flowback-frontend, to access the buttons for the generators you put
PUBLIC_FLOWBACK_AI_MODULE = TRUE

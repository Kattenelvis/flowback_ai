from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .AI_models.proposal import proposals
from .AI_models.prediction_statement import prediction_statements
import re
import openai
import os

# Create your views here.
class AIViewAPI(APIView):
    def post(self, request):

        prompt = request.data.get('prompt')
        
        proposals_response = proposals(prompt)

        predictions = prediction_statements(proposals_response.content)
        
        proposal_response_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', proposals_response.content, re.DOTALL)
        
        prediction_response_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', predictions.content, re.DOTALL)

        return Response(status=status.HTTP_200_OK, data={"proposals": proposal_response_array, "predictions":prediction_response_array })
    
        # responseArray =["Implement strict water conservation measures city-wide.\n",
        #     "Invest in desalination plants to produce more drinking water.\n",
        #     "Increase water recycling and reuse programs.\n",
        #     "Enforce regulations on industries to reduce their water consumption.\n",
        #     "Explore new sources of water such as capturing rainwater or sourcing water from nearby lakes/rivers."]

        # responseArray = """Implement strict water conservation measures city-wide.\n",
        #     "Invest in desalination plants to produce more drinking water.\n",
        #     "Increase water recycling and reuse programs.\n",
        #     "Enforce regulations on industries to reduce their water consumption.\n",
        #     "Explore new sources of water such as capturing rainwater or sourcing water from nearby lakes/rivers.
        #     """

    #How do I increase sales on bananas by 3% over the upcoming 3 weeks
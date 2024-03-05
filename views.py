from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .proposalsAI import test
import re


# Create your views here.
class AIViewAPI(APIView):
    def post(self, request):
        prompt = request.data.get('prompt')
        
        # response = test(prompt)

        # responseArray = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', response.content, re.DOTALL)

        responseArray =["Implement strict water conservation measures city-wide.\n",
            "Invest in desalination plants to produce more drinking water.\n",
            "Increase water recycling and reuse programs.\n",
            "Enforce regulations on industries to reduce their water consumption.\n",
            "Explore new sources of water such as capturing rainwater or sourcing water from nearby lakes/rivers."]


        return Response(status=status.HTTP_200_OK, data=responseArray)
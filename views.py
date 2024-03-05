from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .AI_models.proposal import proposals
from .AI_models.prediction_statement import prediction_statements
from .AI_models.prediction_bets import prediction_bets
import re

# Create your views here.
class AIViewAPI(APIView):
    def post(self, request):

        prompt = request.data.get('prompt')
        
        proposals_res = proposals(prompt)

        predictions = prediction_statements(proposals_res.content)

        bets = prediction_bets(proposals_res.content, predictions.content)

        proposal_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', proposals_res.content, re.DOTALL)
        
        prediction_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', predictions.content, re.DOTALL)
        
        bets_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', bets.content, re.DOTALL)

        return Response(status=status.HTTP_200_OK, data={"proposals": proposal_array, "predictions": prediction_array, "bets": bets.content })

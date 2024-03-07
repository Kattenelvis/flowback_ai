from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .AI_models.proposal import proposals
from .AI_models.prediction_statement import prediction_statements
from .AI_models.prediction_bets import prediction_bets
from .AI_models.voter import voter
from .AI_models.poll_titles import poll_titles
import re


class AIViewAPI(APIView):
    def post(self, request):

        prompt = request.data.get('prompt')

        poll_titles_res = poll_titles(prompt)
        
        poll_titles_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', poll_titles_res.content, re.DOTALL)

        proposals_res = proposals(poll_titles_array[0])

        predictions = prediction_statements(proposals_res.content)

        bets = prediction_bets(proposals_res.content, predictions.content)

        proposal_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', proposals_res.content, re.DOTALL)
        
        prediction_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', predictions.content, re.DOTALL)
        
        bets_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', bets.content, re.DOTALL)

        voting = voter(proposals_res, predictions, bets)

        return Response(status=status.HTTP_200_OK, data={"titles": poll_titles_array, "proposals": proposal_array, "predictions": predictions.content, "bets": bets.content, "voting":voting.content })


class pollTitleAPI(APIView):
    def post(self, request):
        prompt = request.data.get('prompt')

        poll_titles_response = poll_titles(prompt)
        
        poll_titles_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', poll_titles_response.content, re.DOTALL)

        return Response(status=status.HTTP_200_OK, data={"titles": poll_titles_array})
        
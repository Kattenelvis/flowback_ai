from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .AI_generators.proposal import proposals
from .AI_generators.prediction_statement import prediction_statements
from .AI_generators.prediction_bets import prediction_bets
from .AI_generators.voter import voter
from .AI_generators.poll_titles import poll_titles
from .AI_generators.area import area
import re

class AIViewAPI(APIView):
    def post(self, request):

        title = request.data.get('title')
        area = request.data.get('area')

        proposals_res = proposals(title).content
        proposal_array = proposals_res.split("\n")

        predictions = prediction_statements(proposals_res).content
        prediction_array = predictions.split("\n")

        bets = prediction_bets(proposals_res, predictions).content
        bets_array = bets.split("\n")

        voting = voter(proposals_res, predictions, bets).content
        voting_array = voting.split("\n")

        return Response(status=status.HTTP_200_OK, data={
            "proposals": proposal_array, 
            "predictions": prediction_array, 

            "bets": bets_array,

            "voting":voting_array })


class pollTitleAPI(APIView):
    def post(self, request):
        prompt = request.data.get('prompt')

        poll_titles_response = poll_titles(prompt)        
        poll_titles_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', poll_titles_response.content, re.DOTALL)

        poll_areas_response = area(f"Title:{prompt}; Areas to choose from: Uncategorized, Housing, Economy, Environment, Social Studies, Education, Pool Parties, Recreation, Culture")
        poll_areas_array = re.findall(r'\d+\.\s(.*?)(?=\d+\.\s|\Z)', poll_areas_response.content, re.DOTALL)


        return Response(status=status.HTTP_200_OK, data={"titles": poll_titles_array, "areas":poll_areas_array})
        

class proposalAPI(APIView):
    def post(self, request):
        prompt = request.data.get('prompt')
        print(prompt, "PROOMPT")

        proposals_res = proposals(prompt).content
        proposal_array = proposals_res.split("\n")

        return Response(status=status.HTTP_200_OK, data={"proposal": proposal_array[0]})
        

class prediction_statementAPI(APIView):
    def post(self, request):
        prompt = request.data.get('prompt')

        predictions = prediction_statements(prompt).content
        prediction_array = predictions.split("\n")

        return Response(status=status.HTTP_200_OK, data={"predictions": prediction_array[0]})
        

class prediction_betsAPI(APIView):
    def post(self, request):
        proposals = request.data.get('proposals')
        predictions = request.data.get('predictions')
        

        bets = prediction_bets(proposals, predictions).content
        bets_array = bets.split("\n")

        return Response(status=status.HTTP_200_OK, data={"bets": bets_array})
        

        
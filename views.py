from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .helper import test

# Create your views here.
class AIViewAPI(APIView):
    def get(self, request):

        test()

        return Response(status=status.HTTP_200_OK, data="45")

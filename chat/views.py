from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class Index(APIView):
    pass

class Room(APIView):
    def get(self, request, room):
        pass
from django.shortcuts import render
from django.http import HttpResponse

# Third Party Imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PlayerSerializer
from .models import Player

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Player.objects.all()
        serializer = PlayerSerializer(qs, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Respone(serializer.data)
        return Response(serializer.errors)
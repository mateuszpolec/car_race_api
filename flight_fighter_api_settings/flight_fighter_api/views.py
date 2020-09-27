from django.shortcuts import render
from django.http import HttpResponse

# Third Party Imports
from rest_framework.response import Response
from rest_framework.views import APIView
import time

# Project imports
from .serializers import PlayerSerializer, AuthPlayerSerializer
from .models import Game, Player, AuthPlayer
from .security import make_hash_sha384

class AuthPlayer(APIView):
    def get(self, request, *args, **kwargs):
        game = Game.objects.all().last()
        if(game):
            print("GAME FOUND")
            if(game.players > 64):
                data = {"status": 400, "token": "", "error": "Too many players on server!"}
            else:
                token = {"timestamp": int(time.time()), "game_uid": game.uid, "game_player": game.players+1}
                token_hash = make_hash_sha384(token)
                game.players += 1
                game.save()
                data = {"status": 200, "token": token_hash}
        else:
            Game.objects.create(uid = 1, is_active = True, players = 1)
            game = Game.objects.all().last()
            token = {"timestamp": int(time.time()), "game_uid": game.uid, "game_player": game.players}
            token_hash = make_hash_sha384(token)
            data = {"status": 200, "token": token_hash}
        return Response(data)

class PlayerView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Player.objects.all()
        serializer = PlayerSerializer(qs, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PlayerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Respone(serializer.data)
        return Response(serializer.errors)
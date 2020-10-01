from django.shortcuts import render
from django.http import HttpResponse

# Third Party Imports
from rest_framework.response import Response
from rest_framework.views import APIView
import time

# Project imports
from .serializers import PlayerSerializer
from .models import Game, Player
from .security import make_hash_sha384

class AuthPlayerView(APIView):
    def get(self, request, *args, **kwargs):
        game = Game.objects.all().last()
        if(game):
            if(game.players > 64):
                data = {"status": 400, "token": "", "error": "Too many players on server!"}
            else:
                token = {"timestamp": int(time.time()), "game_uid": game.uid, "game_player": game.players+1}
                token_hash = make_hash_sha384(token)
                game.players += 1
                game.save()
                data = {"status": 200, "token": token_hash}
                Player.objects.create(token = token_hash, x_position = 1, y_position = 1)
        else:
            Game.objects.create(uid = 1, is_active = True, players = 1)
            game = Game.objects.all().last()
            token = {"timestamp": int(time.time()), "game_uid": game.uid, "game_player": game.players}
            token_hash = make_hash_sha384(token)
            data = {"status": 200, "token": token_hash}
            Player.objects.create(token = token_hash, x_position = 1, y_position = 1)
        return Response(data)

class PlayerView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Player.objects.all()
        serializer = PlayerSerializer(qs, many = True)
        return Response(serializer.data)


    def patch(self, request, *args, **kwargs):
        serializer = PlayerSerializer(data = request.data)
        if serializer.is_valid():
            token = serializer.data['token']
            player = Player.objects.filter(token = token).last()
            player.x_position = serializer.data['x_position']
            player.y_position = serializer.data['y_position']
            player.save()
            return Response(serializer.data)
        print(serializer.data)
        return Response(serializer.errors)
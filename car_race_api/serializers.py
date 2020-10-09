from rest_framework import serializers

from .models import Player

from django import forms


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'token', 'time_map1', 'time_map2'
        )
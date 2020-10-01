from rest_framework import serializers

from .models import Player

from django import forms


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'token', 'x_position', 'y_position'
        )
from rest_framework import serializers

from .models import Player, AuthPlayer

from django import forms

class AuthPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPlayer
        fields = [
            'token'
        ]

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'x_position', 'y_position', 'owner', 'timestamp'
        )
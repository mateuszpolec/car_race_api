from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Game(models.Model):
    uid = models.IntegerField(default = 1, editable = False)
    is_active = models.BooleanField(default = False)
    players = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(64)], default = 0)

    def __str__(self):
        return f"Game number {self.uid}"



class Player(models.Model):
    token = models.CharField(max_length = 96, default = "", null = True)
    time_map1 = models.FloatField(null = True)
    time_map2 = models.FloatField(null = True)

    def __str__(self):
        return f"Token {self.token} x pos: {self.time_map1}, y pos: {self.time_map2}"
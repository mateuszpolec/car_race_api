from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Game(models.Model):
    uid = models.IntegerField(default = 1)
    is_active = models.BooleanField(default = False)
    players = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(64)], default = 0)

    def __str__(self):
        return f"Game number {self.uid}"

class AuthPlayer(models.Model):
    token = models.CharField(max_length = 96)

    def __str__(self):
        return self.token

class Player(models.Model):
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    timestamp = models.DateTimeField(default = timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.x_position)
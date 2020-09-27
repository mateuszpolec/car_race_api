from django.contrib import admin

from .models import Game, Player, AuthPlayer

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('uid', 'is_active', 'players')

admin.site.register(Player)
admin.site.register(AuthPlayer)
from django.contrib import admin

from .models import User, Team, Game, Card

# Register your models here.
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Card)
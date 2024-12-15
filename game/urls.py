from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gamelist/<str:team>", views.game_list, name="game_list"),
    path("<str:team>/newgame", views.new_game, name="new_game"),
    path("<int:game_id>/submitcard", views.submit_card, name="submit_card"),
    path("board/<int:game_id>/", views.game_board, name="game_board"),
]
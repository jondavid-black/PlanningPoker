from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse

from .models import Team, Game, User, Card

# Create your views here.
def index(request):
    teams = Team.objects.all()
    template = loader.get_template("game/index.html")
    context = {
        "teams": teams,
    }
    return HttpResponse(template.render(context, request))

def game_list(request, team):
    games = get_list_or_404(Game, team__name=team)
    list_of_games = f"<h1>Games for {team}</h1>"
    template = loader.get_template("game/gamelist.html")
    context = {
        "team": team,
        "games": games,
    }
    return HttpResponse(template.render(context, request))

def new_game(request, team):
    team = get_object_or_404(Team, name=team)
    game_name = request.POST["game_name"]
    game = Game.objects.create(name=game_name, team=team)
    return HttpResponseRedirect(reverse("game_list", args=(team,)))

def game_board(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    cards = Card.objects.filter(game=game)
    team = get_object_or_404(Team, name=game.team)
    template = loader.get_template("game/board.html")
    context = {
        "game": game,
        "cards": cards,
        "users": team.users.all(),
    }
    return HttpResponse(template.render(context, request))

def submit_card(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    user_name = request.POST["user_name"]
    user = User.objects.get(name=user_name)
    value = request.POST["card_value"]
    card = Card.objects.create(value=value, user=user, game=game)
    return HttpResponseRedirect(reverse("game_board", args=(game.id,)))

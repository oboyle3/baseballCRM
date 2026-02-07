from django.shortcuts import render
from .models import Team, Player
# Create your views here.
def landing(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    print(players)
    context = {
        "teams": teams,
        "players":players,
    }
    return render(request, "league/landing.html",context )


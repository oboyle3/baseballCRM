from django.shortcuts import render
from .models import Team, Player ,Minor, Prospect
from .forms import PlayerStatForm
# Create your views here.
def landing(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    minor_teams = Minor.objects.all()
    prospect = Prospect.objects.all()
    print(players)
    print(minor_teams)
    context = {
        "teams": teams,
        "players":players,
        "minor_teams": minor_teams,
        "prospect":prospect
    }
    return render(request, "league/landing.html",context )

def hello_post(request):
    name = None
    if request.method == "POST":
        name = request.POST.get("name")
        #request.POST is a dictionary

    return render(request, "league/hello.html", {"name": name})

def add_team(request):
    
    if request.method == "POST":
        name = request.POST.get("name")
        city = request.POST.get("city")
        if name and city:
            Team.objects.create(
                name=name,
                city=city
            )
    teams = Team.objects.all()

    return render(request,"league/add_team.html",{
        "teams":teams})


def player_comparison(request):
    
    players = Player.objects.all()
    player1 = None
    player2 = None
    print(players)
    if request.method == "POST":
        p1_id = request.POST.get("player1")
        p2_id = request.POST.get("player2")
        if p1_id and p2_id:
            player1 = Player.objects.get(id=p1_id)
            player2 = Player.objects.get(id=p2_id)
    context = {
        
        "players":players,
        "player1": player1,
        "player2": player2,
        
    }
    return render(request, "league/player_comparison.html",context )



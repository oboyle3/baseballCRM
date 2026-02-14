from django.shortcuts import render
from .models import Team, Player ,Minor, Prospect,Gaa_Team
from .forms import PlayerStatForm
# Create your views here.
def landing(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    minor_teams = Minor.objects.all()
    prospect = Prospect.objects.all()
    gaa_team = Gaa_Team.objects.all()
    print(players)
    print(minor_teams)
    context = {
        "teams": teams,
        "players":players,
        "minor_teams": minor_teams,
        "prospect":prospect,
        "gaa_team":gaa_team,
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


def gaa_comp(request):
    gaa_team = Gaa_Team.objects.all()
    team1 = None
    team2 = None
    winner = None
    team1_obj = None
    team2_obj = None
    if request.method == "POST":
        team1 = request.POST.get("Team1")
        team2 = request.POST.get("Team2")
        print(f"team1={team1} , team2={team2}")
        if team1 and team2:
            team1_obj = Gaa_Team.objects.get(id=team1)
            team2_obj = Gaa_Team.objects.get(id=team2)
            print(f"{team1_obj} vs. {team2_obj}")
            if team1_obj.rating > team2_obj.rating:
                winner = team1_obj
                print(f"{team1_obj.rating}  = team1_obj.rating")
                print(f"{team2_obj.rating}  = team2_obj.rating")
                print(f"{team1_obj} is winner. congrats")

            elif team2_obj.rating > team1_obj.rating:
                winner = team2_obj
                print(f"{team2_obj} is the winner I think")
            else:
                winner = "draw"

    context = {    
        "gaa_team":gaa_team,
        "team1": team1_obj,
        "team2": team2_obj,
        "winner": winner,
    }
    return render(request, "league/gaa_comp.html",context )

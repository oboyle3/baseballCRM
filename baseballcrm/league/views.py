from django.shortcuts import render
from .models import Team, Player
from .forms import PlayerStatForm
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





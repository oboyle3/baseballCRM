from django.shortcuts import render
from .models import Team
# Create your views here.
def landing(request):
    teams = Team.objects.all()
    return render(request, "league/landing.html", {"teams": teams})
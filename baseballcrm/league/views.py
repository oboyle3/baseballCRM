from django.shortcuts import redirect, render
from .models import Team, Player ,Minor, Prospect,Gaa_Team, News, Conference, NCAA_TEAM, NCAA_Player, Stock
from .forms import Stockform
import pandas as pd
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from .forms import UploadFileForm
import numpy as np
import os
# Create your views here.
def landing(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    minor_teams = Minor.objects.all()
    prospect = Prospect.objects.all()
    gaa_team = Gaa_Team.objects.all()
    conference = Conference.objects.all()
    ncaa_teams = NCAA_TEAM.objects.all()
    news = News.objects.filter(is_active=True)[:5]
    
    
    context = {
        "teams": teams,
        "players":players,
        "minor_teams": minor_teams,
        "prospect":prospect,
        "gaa_team":gaa_team,
        "news": news,
        "conference": conference,
        "ncaa_teams": ncaa_teams,
   
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
    counter = 0
    if request.method == "POST":
        team1 = request.POST.get("Team1")
        team2 = request.POST.get("Team2")
        print(f"team1={team1} , team2={team2}")
        if team1 and team2:
            counter = counter + 1
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


def testing_Screen(request):
    if request.method == "POST":
        form = Stockform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("landing")
    else:
        form = Stockform()
    counter = 0
    stock = Stock.objects.all()
    print(stock)
    context = {    
        "stock":stock,
        "form": form,
        
    }
    return render(request, "league/testing_Screen.html",context )





def upload_excel(request):

    chart_path = None

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():

            excel_file = request.FILES['file']

            # read excel
            df = pd.read_excel(excel_file)

            players = df['Players_Name']

            made_no = df['Threes_Made_No_Dribble_Before_Shot']
            miss_no = df['Threes_Missed_No_Dribble_Before_Shot']

            made_yes = df['Threes_Made_Yes_Dribble_Before_Shot']
            miss_yes = df['Threes_Missed_Yes_Dribble_Before_Shot']

            x = np.arange(len(players))
            width = 0.2

            plt.figure(figsize=(10,6))

            plt.bar(x - width, made_no, width, label="Made No Dribble")
            plt.bar(x, miss_no, width, label="Missed No Dribble")
            plt.bar(x + width, made_yes, width, label="Made Dribble")
            plt.bar(x + 2*width, miss_yes, width, label="Missed Dribble")

            plt.xticks(x, players, rotation=45)

            plt.title("3PT Shooting Comparison")
            plt.legend()

            plt.tight_layout()

            chart_path = "static/chart.png"
            plt.savefig(chart_path)
            plt.close()

    else:
        form = UploadFileForm()

    return render(request, "league/upload.html", {"form": form, "chart": chart_path})


import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from .forms import UploadFileForm


def upload_portfolio(request):

    chart_path = None
    portfolio_value = None
    total_profit = None
    table_data = None

    if request.method == "POST":

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():

            excel_file = request.FILES['file']

            # Read Excel
            df = pd.read_excel(excel_file)

            # ---- DATA PROCESSING ----

            df["Current_Value"] = df["Shares"] * df["Current_Price"]
            df["Invested_Value"] = df["Shares"] * df["Buy_Price"]
            df["Profit"] = df["Current_Value"] - df["Invested_Value"]

            portfolio_value = df["Current_Value"].sum()
            total_profit = df["Profit"].sum()

            table_data = df.to_dict("records")

            # ---- CHART ----

            plt.figure()

            plt.bar(df["Ticker"], df["Current_Value"])

            plt.title("Portfolio Value by Stock")
            plt.ylabel("Value ($)")

            chart_path = "static/chart.png"
            plt.savefig(chart_path)
            plt.close()

    else:
        form = UploadFileForm()

    return render(request, "league/upload_portfolio.html", {
        "form": form,
        "chart": chart_path,
        "portfolio_value": portfolio_value,
        "total_profit": total_profit,
        "table_data": table_data
    })
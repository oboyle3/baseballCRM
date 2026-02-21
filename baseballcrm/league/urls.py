from django.urls import path
from . import views
from .views import landing, hello_post, add_team, player_comparison, gaa_comp

urlpatterns = [
    path("", landing, name="landing"),
    path("hello/", views.hello_post, name="hello_post"),
    path("player_comparison/", views.player_comparison, name="player_comparison"),
    path("gaa_comp/", views.gaa_comp, name="gaa_comp"),
    path("testing_Screen/", views.testing_Screen, name="testing_Screen"),
]

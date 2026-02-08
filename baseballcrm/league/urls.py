from django.urls import path
from . import views
from .views import landing, hello_post, add_team

urlpatterns = [
    path("", landing, name="landing"),
    path("hello/", views.hello_post, name="hello_post"),
    
]

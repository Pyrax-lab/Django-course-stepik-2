from django.urls import path 
from . import views

app_name = "hr"


urlpatterns = [
   path("", views.main, name="main"),
]
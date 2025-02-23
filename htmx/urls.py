from django.urls import path
from htmx import views

urlpatterns = [
    path('', views.book_list, name="book_list"),
    path('create_book/', views.create_book, name="create_book"),
]
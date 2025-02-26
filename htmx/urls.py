from django.urls import path
from htmx import views
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('', views.book_list, name="book_list"),
    path(_('create_book/'), views.create_book, name="create_book"),
]
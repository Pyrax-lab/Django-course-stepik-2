"""
URL configuration for django_orm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from permission import views

from django.conf.urls.i18n import i18n_patterns # Добавляем префикс к url адресу если писать ru/ будет выдана руская версия сайта если en/ то английская

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('hr', include('hr.urls')),
    path('', include('htmx.urls')),
    path("add", views.add_post, name="add_post"),
    path("accounts/", include('django.contrib.auth.urls')),
    path('__debug__/', include(debug_toolbar.urls)), #debugtoolbar
    path("rosetta/", include('rosetta.urls')) # rosetta
)

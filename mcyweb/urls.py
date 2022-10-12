from django.contrib import admin
from django.urls import path
from . import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', main.home),
    path('getlist/', main.returnlist),
    path('getvideo/', main.getvideo),
    path('submitlike/', main.submitlike),
]
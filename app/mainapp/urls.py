from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.stockPicker, name="stockPicker"),
    path("stocketracker/", views.stockTracker, name="stockTracker"),
]

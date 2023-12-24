from django.urls import path
from core import views

app_name = "urls"

urlpatterns = [
    path("", views.index),
]

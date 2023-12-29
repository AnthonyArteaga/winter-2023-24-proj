from django.urls import path
from core import views

app_name = "urls"

urlpatterns = [
    path("", views.index, name="index"), #names this url as "index"
]

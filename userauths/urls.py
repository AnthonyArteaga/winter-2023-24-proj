from django.urls import path
from userauths import views

app_name = "userauths" #reffering to the app this urls belongs to

urlpatterns = [
    path("sign-up/", views.registerView), 
]



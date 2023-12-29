from django.shortcuts import render, redirect
from userauths.forms import UserRegistrationForm

from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.

def registerView(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid(): #checks if form has no errors in it
            newUser = form.save()  #user is saved to the data base, can be seen with admin POV
            username = form.cleaned_data['username']
            messages.success(request, f"Your account has been created successfully.")
            newUser = authenticate(username = form.cleaned_data['email'], #using the email as username
                                   password = form.cleaned_data['password1'])
            login(request, newUser)
            return redirect("../../") #refers to the name given to the url that renders index.html; once a new user is registered goes to home page
    else:
        form = UserRegistrationForm()
        
    
    context = {
        'form': form  #keys can later be referred to from html
    }
    #above code allows us to not have to use basic html forms, but the django provided forms

    return render(request, "userauths/register.html", context)
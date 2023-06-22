from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contact
from django.contrib.auth import authenticate, logout, login

from django.views.decorators.csrf import csrf_protect
# Create your views here.

def display_in_console(statement: str):
    print("-"*100)
    print(statement)
    print("-"*100)


# Create your views here.
def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

@csrf_protect
def contact(request):
    context = dict()
    context["records"] = Contact.objects.all()
    display_in_console(context)
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('msg')
        date = datetime.now()
        display_in_console(f"name: {name}\nemail: {email}\nmessage: {message}\ndate: {date}")
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        context["message"] = "Thanks for feedback. We will contact you within 24 hrs"
        return render(request, "contact.html", context=context)
    return render(request, "contact.html", context=context)

def places(request):
    return render(request, "places.html")

@csrf_protect
def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        display_in_console(f"{username} --- {password}")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "dummy_protected.html")
        else:
            context = {"message": "Login Failed. Please enter correct name and password"}
            return render(request, "login.html", context)
            
    # #scrollTo=jj4lDE-8RYU4
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return HttpResponse("log out user")

def register_user(request):
    return render(request, "signup.html")

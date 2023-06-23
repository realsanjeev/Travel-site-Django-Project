from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contact
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

def display_in_console(statement):
    print("-" * 100)
    print(statement)
    print("-" * 100)

def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

@csrf_protect
def contact(request):
    context = {}
    context["records"] = Contact.objects.all()
    display_in_console(context)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('msg')
        date = datetime.now()
        display_in_console(f"name: {name}\nemail: {email}\nmessage: {message}\ndate: {date}")
        
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        
        context["message"] = "Thanks for your feedback. We will contact you within 24 hrs"
        return render(request, "contact.html", context=context)

    return render(request, "contact.html", context=context)

def places(request):
    return render(request, "places.html")

@csrf_protect
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        display_in_console(f"{username} --- {password}")
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, "dummy_protected.html")
        else:
            context = {"message": "Login Failed. Please enter the correct username and password"}
            return render(request, "login.html", context)
    
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return HttpResponse("Logged out user")

def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")
        display_in_console(f"{username} --- {password}")
        
        if password != confirmpassword:
            context = {"message": "Passwords do not match"}
        else:
            user = User.objects.create_user(username, email, password)
            user.save()
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return render(request, "dummy_protected.html")

    return render(request, "signup.html")

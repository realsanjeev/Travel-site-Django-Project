from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            display_in_console(f"{username} ==== {password}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "dummy_protected.html")
            else:
                context = {"message": "Login Failed. Please enter the correct username and password"}
                return render(request, "login.html", context)
    else:
        form = AuthenticationForm()
    
    context = {"form": form}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    return HttpResponse("Logged out user")

def register_user(request):
    if request.method == "POST":
        
        username = request.POST.get('username')
        print("$"*88)
        email = request.POST.get('email')
        print("$"*88)
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        print("$"*88)
        display_in_console("sfsfs")

        if password == confirm_password:
            # Create the user and perform additional registration logic as needed
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            # Redirect to the protected page after successful registration
            # return redirect("home")
            return render(request, "home.html")
        else:
            context = {"error_message": "Passwords do not match"}
            return render(request, "signup.html", context)

    return render(request, "signup.html")

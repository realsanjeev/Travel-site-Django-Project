import os
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseBadRequest

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User
from account.forms import CustomAuthenticationForm

from account.models import Profile

def display_in_console(statement: str) -> None:
    '''print in console
    '''
    print("-" * 100)
    print(statement)
    print("-" * 100)

# Create your views here.
@csrf_protect
def login_user(request):
    login_template = os.path.join('account', 'login.html')
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "dummy_protected.html")
            else:
                context = {"message": "Login Failed. \
                           Please enter the correct username and password"}
                return render(request, login_template, context)
    else:
        form = CustomAuthenticationForm()
    context = {"form": form}
    return render(request, login_template, context)

@login_required(login_url='/login_url')
def logout_user(request):
    logout(request)
    return HttpResponse("Logged out user")

def register_user(request):
    signup_template = os.path.join("account", "signup.html")
    if request.method == "GET":
        display_in_console("GET mETHOD")
        return render(request, signup_template)
    elif request.method == "POST":
        display_in_console("Register-user")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        display_in_console("$" * 88)

        if password == confirm_password:
            # Create the user and perform additional registration logic as needed
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            login(request, user)
            # Redirect to the protected page after successful registration
            # return redirect("home")
            return render(request, "home.html")
        else:
            context = {"error_message": "Passwords do not match"}
            return render(request, signup_template, context)
    return render(request, signup_template)

def account_view(request):
    # return HttpResponse("ok done")
    records = Profile.objects.all() 
    print(records)
    # for record in records:
    #     print(record.__dict__)
    # pass
    return HttpResponse("Account view")
    

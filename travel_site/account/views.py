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
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == "POST":
        display_in_console("Register-user")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        display_in_console(f"{username} -- {email} -- {password}")

        if password == confirm_password:
            # Create the user and perform additional registration logic as needed
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            Profile.objects.create(user=user).save()
            login(request, user)
            # Redirect to the protected page after successful registration
            # return redirect("home")
            return render(request, "home.html")
        else:
            context = {"error_message": "Passwords do not match"}
            return render(request, signup_template, context)
    return render(request, signup_template)

def account_view(request):
    profile_template = os.path.join("account", "profile.html")
    # return HttpResponse("ok done")
    records = Profile.objects.all() 
    record = Profile.objects.all().first()
    display_in_console(record.__dict__)
    context = {}
    context["user"] = record
    print(records)
    # for record in records:
    #     print(record.__dict__)
    # pass
    return render(request, profile_template, context=context)
    

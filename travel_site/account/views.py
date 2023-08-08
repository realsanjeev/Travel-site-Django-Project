from pathlib import Path
from django.http import HttpResponse, HttpResponseBadRequest
from django.htto.response import render, redirect

# Create your views here.
def login_view(request):
    template_file = Path('login.html')

    return render(request, template_file)

def logout_view(request):
    return redirect('/')

def sign_up_view(request):
    signup_template = Path('signup.html')

    render(request, )

    
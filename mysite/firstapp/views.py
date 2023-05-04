from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    return HttpResponse("This is contact")

def about(request):
    return HttpResponse("This is about")

def home(request):
    return HttpResponse("This is home")
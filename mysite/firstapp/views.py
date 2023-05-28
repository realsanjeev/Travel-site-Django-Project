from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_protect

from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    return HttpResponse("This is contact")

def about(request):
    return HttpResponse("This is about")

def home(request):
    return HttpResponse("This is home")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allow user to be view and edited
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
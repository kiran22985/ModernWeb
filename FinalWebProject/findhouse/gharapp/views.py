from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'gharapp/index.html')

def registeroption(request):
    return render(request, 'gharapp/RegisterOption.html')

def contact(request):
    return render(request, 'gharapp/ContactPage.html')

def room(request):
    return render(request, 'gharapp/RoomPage.html')


def flat(request):
    return render(request, 'gharapp/FlatPage.html')

def viewdetail(request):
    return render(request, 'gharapp/ViewDetails.html')



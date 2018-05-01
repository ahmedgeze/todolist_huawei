from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def homepage(request):
    return render(request,'home.html')

def thanks(request):
    return render(request,'thanks.html')    

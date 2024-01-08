from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("Welcome To Django!")
def about(request):
    return HttpResponse("Welcome To The APP!")
def home(request):
    return HttpResponse("Welcome To Home!")

# Create your views here.


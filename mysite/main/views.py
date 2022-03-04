from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Hello World</h1>")


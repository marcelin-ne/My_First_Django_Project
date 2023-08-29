from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def members(request):
    return render(request, 'members.html')
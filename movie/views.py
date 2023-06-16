from django.shortcuts import render
import requests

# Create your views here.
def index(request,page=1):
    return render(request,'index.html')

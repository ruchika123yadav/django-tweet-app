from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(req):
    return HttpResponse("This is the home of app Tweet")

def tweet(req):
    return render(req,'index.html')
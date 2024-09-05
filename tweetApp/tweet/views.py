from django.shortcuts import render

# Create your views here.


def tweet(req):
    return render(req,'index.html')
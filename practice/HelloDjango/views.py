from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from HelloDjango.models import post

def index(request):
    now = datetime.now()
    variables = {
        'title' : "Hello Django",
        'message' : "Hello Django!",
        'content' : " on " + now.strftime("%A, %d %B, %Y at %X"),
    }

    return render(
        request,
        "index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        variables
    )
def about(request):
    return render(
        request,
        "about.html",
        {
            'title':"about",
            'content':"Example app page for Django."
        }
    )
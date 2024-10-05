from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "massage": "Hello Django Developers",
    }
    return render(request, "myproject1/index.html", context)
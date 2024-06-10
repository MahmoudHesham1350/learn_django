from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello\index.html")

def mahmoud(request):
    return HttpResponse("Hello, Mahmoud!")

def hazem(request):
    return HttpResponse("Hello, Hazem!")

def greet(request, name :str):
    return render(request, "hello\greet.html", {
        "name": name.capitalize(),
    })



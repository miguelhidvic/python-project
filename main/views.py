from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render


def home(request):
    return render(request, "main/home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "main/login.html", {"error": "Invalid username or password"})
    else:
        return render(request, "main/login.html")

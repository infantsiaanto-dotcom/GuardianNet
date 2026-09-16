from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import IncidentForm
from .models import Incident


def report_incident(request):
    if not request.user.is_authenticated:
        return render(request, "auth_required.html", {"next": "/report/"})

    if request.method == "POST":
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.reported_by = request.user
            incident.save()
            return redirect('incident_list')
    else:
        form = IncidentForm()

    return render(request, "report_incident.html", {"form": form})
def incident_list(request):
    incidents = Incident.objects.all().order_by('-created_at')
    return render(request,'incident_list.html',{'incidents': incidents})
def register(request):
    if request.method =="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('incident_list')
    else:
        form=UserCreationForm()
    return render(request,"register.html",{"form":form})            
def user_login(request):
    next_url = request.GET.get('next', '/')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url if next_url.startswith('/') else '/')
        else:
            return render(request, "login.html", {"error": "Invalid credentials", "next": next_url})

    return render(request, "login.html", {"next": next_url})
def user_logout(request):
    logout(request)
    return redirect('home')
def home(request):
    return render(request,"home.html")
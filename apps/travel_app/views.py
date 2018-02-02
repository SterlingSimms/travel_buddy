from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from models import *

def main(request):
    return render(request, "travel_app/main.html")

def add_trip(request):
    return render(request, "travel_app/add_trip.html")

def description(request):
    return render(request, "travel_app/description.html")

def schedule(request):
    return render(request, "travel_app/schedule.html")

def login(request):
    return redirect("/schedule")
    




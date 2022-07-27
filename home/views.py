from aiohttp import request
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request,"home.html")


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return render(request, 'base.html')

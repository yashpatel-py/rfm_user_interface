from django.shortcuts import render
from django.views import generic
from .forms import SignUpUserForm

# Create your views here.
def home(request):
    return render(request, 'main/home.html')
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from .models import Product, Downloads, Reviews
from math import ceil
from .forms import SignUpForm


# added here
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import ProfileForm

from django.urls import reverse_lazy

success_url = reverse_lazy('profile')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# till here

def index(request):
    products = Product.objects.all()
    print(request.GET)
    return render(request, 'carouseltest7.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = SignUpForm()
    return render(request, 'loginpage.html', {'form': form})

@login_required
def profile(request):
    return render(request,'profile.html')


def fort(request):
    download = 'login'
    game = Product.objects.get(product_name = 'Fort')
    print(game.product_desc)
    if request.user.is_authenticated:
        download = game.product_img
        print("allow download")
        print("allow add reviews")
    params = {"download":download}
    return render(request,'fort.html',params)  


def about(request):
    return render(request, 'about.html')

def carouseltest7(request):
    return render(request, 'carouseltest7.html')

def community(request):
    return render(request, 'community.html')

def support(request):
    return render(request, 'support.html')

def base(request):
    return render(request, 'base.html')

  

def apex(request):
     return render(request,'apex.html')

def prince(request):
    return render(request,'prince.html')

def lol(request):
    return render(request,'lol.html')


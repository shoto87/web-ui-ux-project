from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product
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
    n = len(products)
    nSlides = n//4 - ceil(n/4 -n//4 )
    params = {"products":products,"nSlides":nSlides,"range":range(1,nSlides)}
    return render(request, 'carouseltest7.html',params)

# def login(request):
#     return render(request, 'carouseltest7.html')

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        return render(request, 'loginpage.html', {'form': form})




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

def fort(request):
    return render(request,'fort.html')    

def apex(request):
     return render(request,'apex.html')

def prince(request):
    return render(request,'prince.html')

def lol(request):
    return render(request,'lol.html')

def profile(request):
    return render(request,'profile.html')
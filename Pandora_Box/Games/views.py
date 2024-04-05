from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from .models import Product, Downloads, Reviews
from math import ceil
from .forms import SignUpForm
from django.contrib.auth import logout
import base64
# added here
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import ProfileForm,DownloadForm

from django.urls import reverse_lazy

success_url = reverse_lazy('profile')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            first_name = user.first_name
            login_status = user.is_authenticated
            print(login_status)
            email = user.email
            return render(request, 'profile.html', {'first_name': first_name,'email':email})  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# till here

def index(request):
    products = Product.objects.all()
    print(request.GET)
    return render(request, 'home.html')

def signout(request):
    logout(request)    
    return render(request, 'home.html')




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
    print("request.user.is_authenticated",request.path)
    if request.user.is_authenticated:
        download = game.product_img
        print("allow download")
        print("allow add reviews")
    params = {"download":download}
    return render(request,'fort.html',params)  

def game_request(request):
    params = {}
    game_name = request.GET.get('game_type','')
    game = Product.objects.get(product_name = game_name)
    encoded_image = base64.b64encode(game.product_img.read()).decode('utf-8')
    first_name = None
    allow_reviews = False
    if request.user.is_authenticated:
        first_name = request.user.first_name
        downloads = Downloads.objects.filter(product=game,user=first_name)
        print(downloads.count())
        if downloads.count():
            allow_reviews = True

    params={
        'desc' : game.product_desc,
        'image': encoded_image,
        'name': game.product_name,
        'first_name' :  first_name,
        'allow_reviews' : allow_reviews
    }
    return render(request,game_name+'.html',params)

def download_game(request):
    if request.method == 'POST':
        game_name = request.POST.get('download_game','')
        downloads  = Downloads.objects.create(product = game_name,user = request.user.first_name)
        downloads.save()
    print(game_name)
    return render(request,game_name+'.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def community(request):
    return render(request, 'community.html')

def support(request):
    return render(request, 'support.html')

def base(request):
    return render(request, 'base.html')

  

def apex(request):
     return render(request,'Apex Legends.html')

def prince(request):
    return render(request,'Prince Of Persia.html')

def lol(request):
    return render(request,'League Of Legends.html')


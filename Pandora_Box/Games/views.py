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

from django.shortcuts import render
from .models import Review

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})



from django.shortcuts import render
from .models import Review

from django.http import JsonResponse

def review_list(request):
    reviews = Review.objects.all()
    print(reviews)  # Print reviews to the console for debugging
    return render(request, 'review_list.html', {'reviews': reviews})

def success_reviews(request):
    if request.method == 'POST':
        user = request.user
        product_id = request.POST.get('product_id')  # Assuming you're passing product_id in the form
        product = Product.objects.get(id=product_id)
        text = request.POST.get('review_content')
        
        # Save the review
        review = Reviews.objects.create(user=user, product=product, text=text)
        
        # Prepare the response data
        response_data = {
            'user': user.username,
            'text': text,
        }
        
        return JsonResponse(response_data)
    else:
        # Handle other request methods if needed
        pass


def your_view(request):
    reviews = Review.objects.all()  # Assuming you have a Review model
    allow_reviews = True  # Assuming this variable is passed to the template
    return render(request, 'Apex Legends.html', {'reviews': reviews, 'allow_reviews': allow_reviews})


success_url = reverse_lazy('profile')


def login(request):
    params={}
    if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
        }
        
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
    params={}
    if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
    }
    return render(request, 'home.html',params)

def signout(request):
    logout(request)    
    return render(request, 'home.html')




def signup(request):
 params={}
 if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
        } 
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
 params={}
 if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
        }    
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
    if request.user.is_authenticated:
            downloads  = Downloads.objects.create(product = game_name,user = request.user.first_name)
            downloads.save()
    print(game_name)
    return render(request,'success_download.html')

def about(request):
    params={}
    if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
    }
    return render(request, 'about.html',params)

def success_reviews(request):
    params={}
    if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
    }
    return render(request, 'success_reviews.html',params)

def home(request):
    params={}
    if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
        }
    return render(request, 'home.html',params)

def community(request):
    params={}
    if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
        }
    return render(request, 'community.html',params)

def support(request):
    params={}
    if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
        }
    return render(request, 'support.html',params)

def base(request):
    params={}
    if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
        }
    return render(request, 'base.html',params)

  

def apex(request):
    params={}
    if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
        }
    return render(request,'Apex Legends.html',params)

def prince(request):
    params={}
    if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
        }
    return render(request,'Prince Of Persia.html',params)

def lol(request):
    params={}
    if request.user.is_authenticated:
        first_name = request.user.first_name
        params={
        'first_name' :  first_name,
        }
    return render(request,'League Of Legends.html',params)


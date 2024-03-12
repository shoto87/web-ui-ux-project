from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('carouseltest7', views.carouseltest7, name='carouseltest7'),
    path('community', views.community, name='community'),
    path('support', views.support, name='support'),
    path('base', views.base, name='base'),
    path('login', views.login, name='login'),
    path('fort', views.fort, name='fort'),
    path('apex', views.apex,name='apex'),
    path('lol', views.lol,name='lol'),
    path('prince', views.prince,name='prince'),
    path('signup',views.signup,name='signup') 
]
from django.urls import path
from . import views
from .views import login
from django.urls import path, reverse_lazy
from .views import review_list

# added here
success_url = reverse_lazy('profile')
#till here

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),
    path('community', views.community, name='community'),
    path('support', views.support, name='support'),
    path('base', views.base, name='base'),
    path('login', views.login, name='login'),
    path('fort', views.fort, name='fort'),
    path('apex', views.apex,name='apex'),
    path('lol', views.lol,name='lol'),
    path('prince', views.prince,name='prince'),
    path('signup',views.signup,name='signup'),
    path('profile/', views.profile, name='profile'),
    path('signout',views.signout,name='signout'),
    path('game_request',views.game_request,name='game_request'),
    path('download_game',views.download_game,name='download_game'),
    path('success_reviews',views.success_reviews,name='success_reviews'),
    path('reviews/', review_list, name='review_list')


]
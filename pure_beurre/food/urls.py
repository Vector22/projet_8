from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.login,
         {'template_name': 'food/registration/login.html'}, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('result/<str:searchedFood>', views.result, name='result'),
    #path('saveFood/', views.saveFood, name='saveFood'),
    path('all_foods/', views.all_foods, name='all_foods'),
    path('test/', views.test)
    ]

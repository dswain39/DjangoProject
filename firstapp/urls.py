from django.urls import path
from . import views

urlpatterns = [

path('',views.home_view,name='home'),
path('firstapp_home/', views.firstapp_home, name='firstapp_home'),
path('firstapp_home/signin/', views.signin_view, name='signin'),

]

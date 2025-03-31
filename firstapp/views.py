from django.shortcuts import render


# Create your views here.

def home_view(httprequest):
    return render(httprequest, 'home.html')

def firstapp_home(httprequest):
    return render(httprequest, 'firstapp/home.html')

def signin_view(httprequest):
    return render(httprequest, 'firstapp/signin.html')
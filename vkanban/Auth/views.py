from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls.resolvers import re
import pdb


def Login(request):

    if(request.method == "GET"):
        return render(request,"Auth/login.html",{})
    elif(request.method == "POST"):

        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request,email = email,password = password)
        if(user is not None):
            login(request,user)
            #redirect to main page
        else:
            #render(request,"auth/login.html",{}) with context containing wrong password
            pass





def registration(request):
    if(request.method == "GET"):
        return  render(request,"Auth/register.html",{})

    elif(request.method == "POST"):
        
        email = request.POST["email"]
        password = request.POST["password"]

        


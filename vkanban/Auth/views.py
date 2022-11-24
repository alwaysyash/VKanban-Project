from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls.resolvers import re
import pdb

def user_exists(email):
    result_set = User.objects.filter(username = email)
    return result_set.exists()

def Login(request):

    if(request.method == "GET"):
        return render(request,"Auth/login.html",{"error":""})
    elif(request.method == "POST"):

        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(username = email,password = password)
        if(user is not None):
            login(request,user)
            #redirect to main page
        else:
            return render(request,"Auth/login.html",{"error":"Username or password incorrect"}) 
            pass





def registration(request):
    if(request.method == "GET"):
        return  render(request,"Auth/register.html",{"error":""})

    elif(request.method == "POST"):
        email = request.POST["email"]
        password = request.POST["password"]

        if(user_exists(email)):
            
            error_message = {"error":"Email already in use"}
            return render(request,"Auth/register.html",error_message)
        
        else:
            new_user = User.objects.create(username = email,password = password)
            new_user.save()

            #return redirect() to main page
        
        


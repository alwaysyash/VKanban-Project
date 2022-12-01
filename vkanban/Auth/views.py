from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls.resolvers import re
import pdb

def user_exists(username):
    result_set = User.objects.filter(username =username)
    return result_set.exists()

def Login(request):

    if(request.method == "GET"):
        return render(request,"Auth/login.html",{"error":""})
    elif(request.method == "POST"):

        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username = username,password = password)
        if(user is not None):
            login(request,user)
            return redirect("kanban:home")
        else:
            return render(request,"Auth/login.html",{"error":"Username or password incorrect"}) 





def registration(request):
    if(request.method == "GET"):
        return  render(request,"Auth/register.html",{"error":""})

    elif(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]

        if(user_exists(username)):
            
            error_message = {"error":"username already in use"}
            return render(request,"Auth/register.html",error_message)
        
        else:
            new_user = User.objects.create_user(username = username,password = password)

            #return redirect() to main page
        
        


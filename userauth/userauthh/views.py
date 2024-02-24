from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User





def registerUser(req):
    if req.method=='POST':
        fname=req.POST.get("fname","")
        
        
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        
        print(fname,username,password)
        if password:
            if User.objects.filter(username=username).exists():
                messages.info(req,"username already exist")
                return redirect('auth:register')
           
               
            else:
                user=User.objects.create_user(first_name=fname,username=username,password=password)
                user.save()
                return redirect('auth:login')
       
    return render(req, 'registeruser.html')

def loginUser(req):
    if req.method=='POST':
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
          auth.login(req,user)
          print(user)
          req.session['user']=str(user)
          return redirect('shop:home')
        else:
            messages.info(req, "invalidcredentials")
            return redirect('auth:login')
       
    return render(req, 'loginuser.html')
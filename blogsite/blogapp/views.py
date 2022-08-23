from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .models import Post,Profile 
# Create your views here.

def home(request):
    post = Post.objects.all().order_by('-id') 

    for i in post:
        img = i.image 
        print(img) 
    context = {
        'post':post,
    }
    return render(request,'blogapp/home.html',context)  

def register(request):
    if request.method == 'POST': 
        username = request.POST.get('username') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 

        if User.objects.filter(username=username).exists:
            messages.error(request,'Username already taken !')
            return redirect('register')

        user = User(
            username=username,
            email=email,
            
        )
        user.set_password(password) 
        user.save()
        
        messages.success(request,'Registration Successful!') 
        return redirect('login') 

    return render(request,'auth/register.html') 

def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username') 
        password = request.POST.get('password') 

        print(username,password)
        user = authenticate(username=username,password=password) 
        if user != None :
            login(request,user) 
            return redirect('home')
        else:
            messages.error(request,'Username or Password Invali!') 
            return redirect('login') 
    return render(request,'auth/login.html') 

def user_logout(request):
    logout(request) 
    return redirect('home') 

def profile(request,id):
    
    profile = Profile.objects.get(user=id) 

    print(id)  
    print(profile) 

    post = Post.objects.filter(user=id).order_by('-id') 

    print(post) 
    context = {
        'profile':profile, 
        'post':post,
    }
    return render(request,'blogapp/profile.html',context) 


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')

        user_id = request.user.id 
        user = User.objects.get(id=user_id) 
        post = Post(
            user = user,
            title = title,
            desc = desc,
            image = image 
        )
        post.save() 
        messages.success(request,'New Post') 
        return redirect('home') 
    return render(request,'blogapp/create_post.html')

def post_view(request,id):
    post = Post.objects.get(id=id) 
    print(post)
    context = {
        'post':post
    }
    return render(request,'blogapp/post_view.html',context)  
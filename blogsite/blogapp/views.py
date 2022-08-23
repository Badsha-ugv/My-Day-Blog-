from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import  login_required

from .models import Post,BlogUser
# Create your views here.

def home(request):
    post = Post.objects.all().order_by('-id') 

    
    context = {
        'post':post,
    }
    return render(request,'blogapp/home.html',context)  

def register(request):
    if request.method == 'POST': 
        username = request.POST.get('username') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        

        if BlogUser.objects.filter(username=username).exists():
            messages.error(request,'Username already taken !')
            return redirect('register')

        user = BlogUser(
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
    post = Post.objects.filter(user=id)
    user = BlogUser.objects.get(id=id) 

    context = {
        'user':user,
        'post':post
    }
    return render(request,'blogapp/profile.html',context)  

@login_required(login_url='login')
def update_profile(request,id):
    user = BlogUser.objects.get(id=id) 

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        profile = request.FILES.get('profile') 

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email 
        user.profile_pic = profile 
        user.bio = bio 

        if password != None and password != "":
                user.set_password(password)
        if profile != None and profile != "":
            user.profile_pic = profile

        user.save() 
        messages.success(request,'Profile Update Successfully!') 
        return redirect('home') 

    context = {
        'user':user 
    }
    return render(request,'blogapp/update_profile.html',context)  

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')

        user_id = request.user.id 
        user = BlogUser.objects.get(id=user_id) 
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
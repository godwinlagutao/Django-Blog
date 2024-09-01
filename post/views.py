from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm, RegisterForm
from django import forms

# Create your views here.

def home_view(request):
    posts= Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def post_view(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    return render(request, 'post.html', {'blog': blog})

def category_posts(request,foo):
    try:
        category = Category.objects.get(name=foo)
        posts = Post.objects.filter(category=category)
        return render(request, 'category.html', {'posts': posts, 'category':category})
        
    except:
        #messages.success(request, ("Category doesn't exist"))
        return redirect('home_view')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password =password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('home_view')
        
        else:
            messages.success(request, ("There was an error"))
            return redirect('login')
    
    else:
        return render(request, 'login.html', {})
        
  
        
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect('home_view')
    
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home_view')  # Redirect to the home page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def search_posts(request):
    query = request.GET.get('q')
    if query:
        
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    else:
        posts = Post.objects.all()
        
    context = {'posts': posts, 'query': query}
    return render(request, 'search_results.html', context)




@login_required(login_url= 'login')
def create_blog_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post= form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('home_view')
        else:
            form = PostForm()
    
    else:
        form = PostForm()
    return render(request, 'create_blog_post.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import *

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "BlogJay/index.html", context={
        "posts" : posts
    })

def blogpost(request, id):
    try:
        post = get_object_or_404(Post, id=id)
    except:
        return redirect("index")
    
    return render(request, "BlogJay/blogpost.html", context={
        "post": post
    })

def about(request):
    return render(request, "BlogJay/about.html", context=None)

def addPost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect("blogpost", id=post.id)

    else: 
        form = AddPostForm()

    return render(request, "BlogJay/addpost.html", {
        "form": form
    })

def editPost(request, id):
    try: 
        post = get_object_or_404(Post, id=id)
    except: 
        return redirect("index")
    
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("blogpost", id=post.id)

    else:
        form = AddPostForm(instance=post)

    return render(request, "BlogJay/editpost.html", {
        "form": form
    })

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = RegisterForm()

    return render(request, "BlogJay/register.html",{
                  "form": form
    })
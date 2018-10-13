from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
import json
import pandas

# Create your views here.
def post_list(request):
    return render(request, "home/start.html", {})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('show')
    else:
        form = PostForm()
    return render(request, 'home/form.html', {'form': form})

def show(request):
    treports=Post.objects.all()
    k = treports[len(treports)-1]
    #our algorithm
    s = k.source
    d = k.dest

    return HttpResponse("<h1>success</h1>")
    


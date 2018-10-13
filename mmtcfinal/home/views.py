from django.shortcuts import render,redirect
from .forms import PostForm
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
        return redirect('home/form.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'home/form.html', {'form': form})



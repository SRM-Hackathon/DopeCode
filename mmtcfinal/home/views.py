from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
import json
import pandas as pd

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
    file0 = '/home/pavan/DopeCode/mmtcfinal/home/static/FINALFLIGHTTEST.json'
    file1 = '/home/pavan/DopeCode/mmtcfinal/home/static/FINALTRAINTEST.json'
    with open(file0) as flight_file:
        dict_flight = json.load(flight_file)
    flight = pd.DataFrame.from_dict(dict_flight, orient='columns')
    flight.reset_index(level=0, inplace = True)
    with open(file1) as train_file:
        dict_train = json.load(train_file)
    # converting json dataset from dictionary to dataframe
    train = pd.DataFrame.from_dict(dict_train, orient='columns')
    train.reset_index(level=0, inplace=True)
    k = []
    for i in range(0,train.shape[0]):
        b = []
        if train.iloc[i,12] == s.upper():
            if train.iloc[i,7] == d.upper():
                b.append(train.iloc[i,:])
                k.append(b)
    g = []
    for i in range(0,flight.shape[0]):
        b = []
        if flight.iloc[i,7] == s:
            if flight.iloc[i,10] == d:
                b.append(flight.iloc[i,:])
                g.append(b)
    report = pd.DataFrame()
    for q in k:
        r = pd.DataFrame(q)
        report = pd.concat([report,r], axis = 0)
    t = []
    for i in range(0,len(report)):
        p = list(report.iloc[i,:])
        t.append(p)
    return render(request,"home/result.html",{"t":t})
    


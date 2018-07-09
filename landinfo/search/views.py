from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from search.DBconnection import selectland
from .LandInfotitle import landcolumns
from .forms import SearchForm,SearchFormLocate

sland = selectland()
names = landcolumns()

def one(request, landinfo_id):
    data = sland.selectone(landinfo_id)
    name = names.landname
    return render(request, 'search/one.html',{'app':'ひとつだけ','columns':data,'name':name})
    #return render(request, 'search/one.html',{'app':'ひとつだけ','columns':data,})

def all(request):
    data = sland.selectall()
    return render(request, 'search/all.html',{'columns':data})

def searchforms(request):
    if request.method == "POST":
        formlocate = SearchFormLocate(data=request.POST)
        form = SearchForm(data=request.POST)
        if form.is_valid() :
            #このif文の中に処理を書く
            data = sland.selectsearch(request.POST)
            return render(request, 'search/search.html', {'form': form,'columns':data})
    else:
        form = SearchForm()
    return render(request, 'search/search.html', {'form': form})


def get_title(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = SearchForm()

    return render(request, 'results.html', {'form': form})
        
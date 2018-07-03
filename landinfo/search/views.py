from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from search.DBconnection import selectland
#from .forms import SearchForm
from .forms import SearchForm,SearchFormLocate
def one(request, landinfo_id):
    data = selectland('one',landinfo_id,0,0)
    return render(request, 'search/one.html',{'app':'ひとつだけ','columns':data})

def all(request):
    data = selectland('all',0,0,0)
    return render(request, 'search/all.html',{'columns':data})

def searchforms(request):
    if request.method == "POST":
        formlocate = SearchFormLocate(data=request.POST)
        form = SearchForm(data=request.POST)
        if form.is_valid() or formlocate.is_valid:
            #このif文の中に処理を書く
            data = selectland('search',0,0,request.POST['location'])
            data = selectland('search',0,0,request.POST['title'])
            return render(request, 'search/search.html', {'form': form,'columns':data})
    else:
        form = SearchForm()
    return render(request, 'search/search.html', {'form': form, 'formlocate': formlocate})


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
        
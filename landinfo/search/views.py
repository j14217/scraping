from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from scraping_source.land_info_scraping import land_info_scraping
from search.DBconnection import selectland
#from .forms import SearchForm

def one(request, landinfo_id):
    data = selectland('one',landinfo_id)
    return render(request, 'search/one.html',{'app':'ひとつだけ','columns':data})

def all(request):
    data = selectland('all',0)
    return render(request, 'search/all.html',{'app':'全て','columns':data})

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
        
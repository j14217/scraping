from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.template import loader
from django.urls import reverse

from search.pagination import paginate
from search.DBconnection import selectland
from search.LandInfotitle import landcolumns

from .forms import SearchForm
from .models import LandInfo

sland = selectland()
names = landcolumns()

def one(request, landinfo_id):
    data = sland.selectone(landinfo_id)
    name = names.landname
    return render(request, 'search/one.html',{'columns':data,'name':name})


def index(request):
    return render(request,'search/index.html',{'all':'./all/?page=1','search': './searchforms/?page=1'})


def all(request):
    data = sland.selectall()
    allpage = paginate(data,request)
    pdata = allpage.page.object_list
    return render(request, 'search/all.html', {'columns':pdata , 'contacts': allpage.contacts})

def searchforms(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid() :
            f = [
                form.cleaned_data['title'],
                form.cleaned_data['location'],
                form.cleaned_data['traffic'],
                form.cleaned_data['order'],
                form.cleaned_data['min_price'],
                form.cleaned_data['max_price'],
                form.cleaned_data['min_area'],
                form.cleaned_data['max_area'],
            ]
            request.session['search_form'] = f
            return redirect('search:search_result')
    else:
        form = SearchForm()
    return render(request, 'search/search.html', {'form': form})
        
def search_result(request):
    if 'search_form' in request.session:
        f = request.session['search_form']
        form_data = ({
            'title': f[0],
            'location': f[1],
            'traffic': f[2],
            'order':f[3],
            'min_price': f[4],
            'max_price': f[5],
            'min_area': f[6],
            'max_area': f[7],
        })

        form = SearchForm(form_data)

        data = sland.selectsearch(form_data)
        searchpage = paginate(data,request)
        sdata = searchpage.page.object_list
        return render(request, 'search/search.html', {
            'form': form,
            'columns': sdata, 
            'contacts': searchpage.contacts
        })
    else:
        return redirect('search:searchforms')
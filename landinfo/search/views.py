from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from search.models import LandInfo


# Create your views here.
def index(request):
    latest_landinfo_list = LandInfo[:5]
    template = loader.get_template('search/index.html')
    context = {
        'latest_landinfo_list': latest_landinfo_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, landinfo_id):
    try:
        landinfo = LandInfo.objects.get(pk=landinfo_id)
    except LandInfo.DoesNotExist:
        raise Http404("土地が見つかりません")
    return render(request, 'search/detail.html', {'landinfo': landinfo})


def results(request, landinfo_id):
    landinfo = get_object_or_404(LandInfo, pk=landinfo_id)
    return render(request, 'search/results.html', {'landinfo': landinfo})


def retrieval(request, landinfo_id):
    landinfo = get_object_or_404(LandInfo, pk=landinfo_id)
    try:
        selected_landinfo = landinfo.landinfo_set.get(pk=request.POST['landinfo'])
    except (KeyError, LandInfo.DoesNotExist):
        return render(request, 'search/detail.html', {
            'landinfo': landinfo,
            'error_message': "You didn't select a choice",
        })
    else:
        return HttpResponseRedirect(reverse('search:results', args=(landinfo.id,)))

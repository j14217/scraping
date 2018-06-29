from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import LandInfo

class IndexView(generic.ListView):
    template_name = 'search/index.html'
    context_object_name = 'latest_title'

    def get_queryset(self):
        return LandInfo.objects.order_by('-price') [:5]

class DetailView(generic.DetailView):
    model = LandInfo
    template_name= 'search/detail.html'

class ResultView(generic.DetailView):
    model = LandInfo
    template_name = 'search/results.html'

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

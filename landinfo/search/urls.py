from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    # ex: /search/
    path('', views.index, name='index'),

    path('<int:landinfo_id>/results/', views.results, name='results'),

#    path('<int:landinfo>/retrieval', views),
]


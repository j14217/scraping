from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    # ex: /search/
    path('', views.IndexView.as_view(), name='index'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),

    path('<int:landinfo_id>/retrieval', views.retrieval, name='retrieval'),
]


from django.urls import path

from . import views

app_name = 'cApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('n2w/', views.n2w, name='n2w'),
    path('w2n/', views.w2n, name='w2n'),
]
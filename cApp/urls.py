from django.urls import path, include

from . import views

app_name = 'cApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('n2w/', views.n2w, name='n2w'),
    path('w2n/', views.w2n, name='w2n'),
    # path('friends/', views.friends, name='friends'),
    # path('oauth/', include('social_django.urls', namespace='social')),
    # path('complete/<backend>', views.register_by_access_token, name='complete'),
    # path('logout/', views.logout, name='logout'),
]
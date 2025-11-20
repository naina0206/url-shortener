from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('s/<str:code>/', views.redirect_url, name='redirect'),
    path('stats/<str:code>/', views.stats, name='stats'),
]

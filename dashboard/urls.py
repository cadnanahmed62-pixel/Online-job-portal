
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('reports/', views.reports, name='reports'),
]

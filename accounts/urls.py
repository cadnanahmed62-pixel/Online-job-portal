
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('my-profile/', views.job_seeker_profile, name='job_seeker_profile'),
    path('my-profile/', views.job_seeker_profile, name='my_profile'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register,
        name='teacher_registration'),
    path('', views.profile_view, name='profile'),
    path('login/', views.authentication, name='authentication'),
]

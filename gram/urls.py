from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='gram-home'),
    path('about/', views.about ,name='gram-about'),
]
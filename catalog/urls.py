from django.urls import path
from . import views

urlpatterns = [
    path('tvshows/', views.tvshow_list, name='tvshow_list'),
    path('tvshows/<int:pk>/', views.tvshow_details, name='tvshow_details'),
    path('about/', views.about, name='about'),
]

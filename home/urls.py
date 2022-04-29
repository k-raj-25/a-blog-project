from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('photography/', views.photography),
    path('blog/<int:pk>/', views.post),
]
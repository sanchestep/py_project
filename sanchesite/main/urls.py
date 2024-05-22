from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('me/', views.me, name = 'me'),
    path('problem/', views.problem, name = 'problem')
]
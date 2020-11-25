from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<slug:id>/', views.news, name='news'),
    path('allpost/', views.allpost, name='allpost'),
    path('cat/<slug:id>/', views.newscat, name='cat'),
    path('search=<str:pk>/', views.search, name='search'),
    path('newsposter/', views.newsposter, name='newsposter'),
]
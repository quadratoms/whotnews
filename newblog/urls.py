from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
path('', views.home, name='home'),
path('profile/<slug:id>/', views.profile, name='profile'),
path('article/<slug:id>/', views.article, name='article'),
path('article-cat/<slug:id>/', views.cat, name='cat'),
path('edit-article<slug:id>/', views.create_or_edit_post, name='create_or_edit_post'),
path('create-article/', views.create_or_edit_post, name='create_or_edit_post'),
path('registration/', views.register, name='register'),
path('edit/', views.edit_profile, name='edit'),
path('logout/', views.user_logout, name='logout'),
path ( "password_reset" , views.password_reset_request, name = "password_reset" )
]

from django.urls import path
from .views import allnews, news, newscat, comment, catlist, search, top

urlpatterns = [
    path('allnews/', allnews),
    path('top/', top),
    path('news/<slug:id>/', news),
    path('comment/<slug:id>/', comment),
    path('cat/<slug:id>/', newscat),
    path('catlist/', catlist),
    path('search=<str:pk>/', search),
    #path('newsposter/', newsposter),
    ]
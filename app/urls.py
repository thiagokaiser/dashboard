from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),        
    url(r'^logout/$', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='logout'), 
    url(r'^profile/$', views.Profile , name='profile'),
    url(r'^profile/edit/$', views.Edit_profile , name='edit_profile'),
    url(r'^register/$', views.Register , name='register'),
    url(r'^change-password/$', views.Change_Password , name='change-password'),
]

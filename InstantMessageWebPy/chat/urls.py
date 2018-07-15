from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^profile/$', views.profile, name='profile'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^chat_view/$', views.chat_view, name='chat_view'),
    url(r'^changepsw/$', views.changepsw, name='changepws'),
    url(r'^change_pass/$', views.change_pass, name='change_pass'),
    url(r'^mailbox/$', views.mailbox, name='mailbox'),
    url(r'^mail_detail/$', views.mail_detail, name='mail_detail'),
    url(r'^mail_compose/$', views.mail_compose, name='mail_compose'),
    url(r'^graph_echarts/$', views.graph_echarts, name='graph_echarts'),
    url(r'^index24/$', views.index24, name='index24'),
    url(r'^login/$', views.login, name='login'),
    url(r'^loginVerify/$', views.loginVerify, name='loginVerify'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^logout_chat/$', views.logout_chat,name='logout_chat'),
    url(r'^register/$', views.register, name='register'),
    url(r'^regverify/$', views.regverify, name='regverify'),
    url(r'^$', views.index, name='index23'),
    url(r'^(?P<room_name>[^/]+)/(?P<user_name>[^/]+)/$', views.room, name='room'),
    url(r'^userprofile/(?P<username>[^/]+)/$', views.userprofile, name='userprofile'),
    url(r'^(?P<username>[^/]+)/friendprofile/(?P<friendname>[^/]+)/$', views.friendprofile, name='friendprofile'),
    url(r'^(?P<username>[^/]+)/$', views.back2chat, name='back2chat'),
    url(r'^admin/', admin.site.urls),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


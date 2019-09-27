from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
    url(r'^hello/$', views.hello_world, name='hello_world'),
    url(r'^hello2/$', views.hello_world2, name='hello_world2'),
    url(r'^pessoa/$', views.pessoa, name='pessoa'),
    url(r'^pessoa2/$', views.pessoa2, name='pessoa2'),
    url(r'^pessoa3/$', views.pessoa3, name='pessoa3'),
    url(r'^teste/$', views.teste, name='teste'),
]
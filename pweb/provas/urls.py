from django.conf.urls import url

from . import views

app_name = 'provas'
urlpatterns = [
    url(r'^provas/$', views.provas, name='provas'),
    url(r'^submeter/$', views.submeter, name='submeter'),
]
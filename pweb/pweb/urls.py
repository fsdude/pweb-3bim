"""pweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from provas.views import VisualizarProvaView, ResponderProvaFormView, SubmitView, ProvaFormView, QuestaoFormView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^provas/(?P<id>\d+)$', VisualizarProvaView.as_view(), name='visualizar_prova'),
    url(r'^provas/(?P<id>\d+)/responder', ResponderProvaFormView.as_view(), name='responder_prova'),
    url(r'^add', SubmitView.as_view(), name='submit'),
    url(r'^prova/submit', ProvaFormView.as_view(), name='prova'),
    url(r'^questao/submit', QuestaoFormView.as_view(), name='questao'),
]

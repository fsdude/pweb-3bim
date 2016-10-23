from django.conf.urls import url

from . import views

app_name = 'provas'
urlpatterns = [
    url(r'^add', views.SubmitView.as_view(), name='submit'),
    url(r'^provas/(?P<id>\d+)$', views.VisualizarProvaView.as_view(), name='visualizar_prova'),
    url(r'^provas/(?P<id>\d+)/responder', views.ResponderProvaFormView.as_view(), name='responder_prova'),
    url(r'^prova/submit', ProvaFormView.as_view(), name='prova'),
    url(r'^questao/submit', QuestaoFormView.as_view(), name='questao'),
]
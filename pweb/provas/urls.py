from django.conf.urls import url

from . import views

app_name = 'provas'
urlpatterns = [
    url(r'^add', views.SubmitView.as_view(), name='submit'),
    #url(r'^provas', views.visualizarProvas, name='visualizar_provas'),
    url(r'^prova/submit', ProvaFormView.as_view(), name='prova'),
    url(r'^questao/submit', QuestaoFormView.as_view(), name='questao'),
    url(r'^alternativa/submit', AlternativaFormView.as_view(), name='alternativa'),
]
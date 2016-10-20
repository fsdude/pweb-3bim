from django.conf.urls import url

from . import views

app_name = 'provas'
urlpatterns = [
    url(r'^$', views.SubmitView.as_view(), name='submit'),
    url(r'^prova/submit', ProvaFormView.as_view(), name='prova'),
    url(r'^questao/submit', QuestaoFormView.as_view(), name='questao'),
    url(r'^alternativa/submit', AlternativaFormView.as_view(), name='alternativa'),
]
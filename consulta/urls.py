from django.urls import path

from . import views

app_name='consulta'

urlpatterns = [
    path("", views.consulta, name='consulta'),
    path('ensalamento_labs/', views.mostrarEnsalamentoLabs, name="ensalamento_labs"),
    path('ensalamento_labs_nome/', views.mostrarEnsalamentoLabsNome, name="ensalamento_labs_nome"),

]

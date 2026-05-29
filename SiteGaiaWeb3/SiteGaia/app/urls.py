from os import name

from django.urls import path

from . import views


urlpatterns = [
    path('',views.home,name='Home'),
    path('equipe/',views.equipe,name='Equipe'),
    path('Apresentação/', views.projetos,name='Projetos'),
    path('contato/',views.contato, name='Contato'),
]
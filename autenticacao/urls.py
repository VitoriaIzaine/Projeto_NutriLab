from django.urls import path
from . import views

urlpatterns = [
    path('ativar_conta/<str:token>/', views.ativar_conta, name="ativar_conta"),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),
    path('sair/', views.sair, name="sair")
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil, name='perfil'),
]
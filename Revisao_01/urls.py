from django.contrib import admin
from django.urls import path
from core.views import home, cadastro, sucesso, login_view, perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('sucesso/', sucesso, name='sucesso'),
    path('login/', login_view, name='login'),
    path('perfil/', perfil, name='perfil'),
]
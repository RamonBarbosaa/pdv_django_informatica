"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Importamos as duas funções que criámos no views.py
from vendas.views import lista_produtos, realizar_venda 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rota para ver a lista
    path('produtos/', lista_produtos, name='lista_produtos'), 
    
    # Rota para a lógica de diminuir o stock (precisa do ID)
    path('vender/<int:produto_id>/', realizar_venda, name='vender_item'),
]
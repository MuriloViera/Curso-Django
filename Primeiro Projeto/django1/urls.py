"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from core import views

# from core.views import index, contato #Importanto as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), 

    #Poderia adicionar os caminhos aqui mesmo, mas não é o certo, o certo é deixar o urls do projeto so com o admin e criar um urls para cada aplicação
    #path('', index), #Indica que caso o usuario acesse esse url, ele vai executar a view INDEX que vai receber a requisição e subir a tela HTML
    #path('contato', contato),
]

handler404 = views.error404  #Aqui eu to lidando com as paginas de erro 404, falando que quando elas existirem eu vou executar uma view la da aplicação core

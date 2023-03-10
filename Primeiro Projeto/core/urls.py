from django.urls import path

from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato),
    path('produto/<int:id>', produto, name='produto') #Essa rota precisa receber um numero inteiro e ela tem um nome para ser encontrada dps
]
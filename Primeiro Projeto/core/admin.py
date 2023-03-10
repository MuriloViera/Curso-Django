from django.contrib import admin
from .models import Produto, Cliente 

class ProdutoAdmin(admin.ModelAdmin): #Isso serve para que se eu queira que la no ADMIN apareça mais campos do que so o primeiro (nesse caso nome como eu deixei a de cliente)
    list_display = ('nome', 'preco', 'estoque')

# Register your models here.
admin.site.register(Produto, ProdutoAdmin) #Fazendo com que ele observe a tabela Produto
admin.site.register(Cliente) #Fazendo com que ele observe a tabela Cliente

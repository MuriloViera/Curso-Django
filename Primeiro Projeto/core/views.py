from django.shortcuts import render
from django.shortcuts import get_object_or_404 #Essa função vai servir pra caso o objeto do cara nao exista, ele da o erro 404

from .models import Produto

# Create your views here.
def index(request): 
    
    #print(request.user) O request carrega muitas informações que podem ser uteis

    produtos = Produto.objects.all() #Recupera do banco todos os objetos de dados criados com o modelo Produto

    context = { #Se eu for passar algo para a pagina html, tem que ser obrigatoriamente um "dicionário", uma lista de objetos 
        'curso' : 'Programação Web com Django Framework',
        'outro' : 'Django é massa!',
        'produtos' : produtos
    }
    return render(request, 'index.html', context)

def produto(request, id):
    #prod = Produto.objects.get(id=id) #Recupera do banco o objeto com o id que eu recebi

    prod = get_object_or_404(Produto, id=id) #Se eu não faço isso, ele da o erro 500, dando o 404 que o padrão para paginas não encontradas.
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    return render(request, '404.html') 

def contato(request): #Uma view que recebe a requisição http sendo feita
    return render(request, 'contato.html') #Renderiza na requisição sendo feita a pagina contato.html
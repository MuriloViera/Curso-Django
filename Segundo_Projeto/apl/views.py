from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto #Importanto a tabela de dados
from django.shortcuts import redirect

# Create your views here.

def index(request):
    context = {
        'produtos': Produto.objects.all() #Basta isso pra eu passar todos objetos existentes na tabela produto
    }
    return render(request, 'index.html', context)


def produto(request):

    if str(request.user) != 'AnonymousUser': 

        if str(request.method) == 'POST': #Se o request estiver vindo como post, ou seja, ta vindo com dados
            form = ProdutoModelForm(request.POST, request.FILES) #Aqui to passando os dados que tao chegando eles para a variavel 'form'
            if form.is_valid():
                #prod = form.save(commit=False) #Pegar os dados do form, poderia ter feito usando o cleaned_data direito tambem

                form.save()#So isso ja salva o form e manda pro model, que manda pro banco

                messages.success(request, 'Produto salvo com sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(request,'Erro ao salvar o produto')    
        else: #Se nao tiver vindo como post ta vindo como get, ou seja ele ta abrindo a pagina sem mandar nada, ai eu insiro um form seco
            form = ProdutoModelForm()


        context = {
            'formProduto' : form 
        }

        return render(request, 'produtos.html', context)
    
    else: 
        return redirect('index')


def contato(request):
    form = ContatoForm(request.POST or None) #Instância da classe criada no forms.py, aonde essa isntância pode conter dados ou não, no caso a primeira vez que ele abre ele nao vai conter, agora caso eu clique la em enviar, ele vai tacar os dados do formulário pra ca e vai criar o formulário com os dados, nao um vazio

    if str(request.method) == 'POST':
        
        if form.is_valid(): 
            """
            Aqui é se eu quiser printar na tela as informações do POST
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')
            """

            form.send_mail() #Enviando o email configurado e com os dados la no form, e se der certo ele vai printar pq to usando o email de console do Django.

            messages.success(request, 'Enviado com sucesso')
            form = ContatoForm() #Limpo o form chamando a função denovo e nao passando nada
        else:
            messages.error(request, 'Erro ao enviar e-mail')    

    context ={
        'formContato': form
    }

    return render(request, 'contato.html', context)

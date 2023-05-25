from django import forms
from django.core.mail.message import EmailMessage #Importação necessaria para mandar email
from .models import Produto #Estou importanto o modelo de dados de Produto pois ele sera atrelado com o formulário ProdutoModelForm

class ContatoForm(forms.Form): #Formulário normal(sem ligação com o banco de dados)
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome : {nome}\n E-mail: {email}\n Assunto: {assunto}\n Mensagem: {mensagem}'

        #Estrutura do email
        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email=email,
            to = ['contato@seudominio.com.br'],
            headers={'Reply-To' : email}
        )

        mail.send()

class ProdutoModelForm(forms.ModelForm): #Ou seja, esse cara nao é um formulario normal, ele é um formulário de um model, ele vai mandar os dados daqui la pra um model (Que no caso é o produto e ele vai tacar no banco)
    class Meta:
        model = Produto #Informando o model o qual receberá os campos para serem guardados no bacno 
        fields = ['nome', 'preco', 'estoque', 'imagem'] #Campos a serem mandados pro model
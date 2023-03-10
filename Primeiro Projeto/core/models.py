from django.db import models

# Create your models here.
class Produto(models.Model): #É como se eu tivesse criando um objeto de um dado do banco de dados (literalmente uma tabela la no db.sqlite3)
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self): #Essa função faz com que cada objeto criado na tabela receba o nome do campo nome dele, se não fica 'Produto object'
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)    

    def __str__(self):
        return f'{self.nome} {self.sobrenome}' #Voce deve se perguntar que diabo é isso o f'' é um metodo de eu formatar LITERALMENTE TUDO que tiver dentro do '' para string, seja variavel ou o que krl for. Se for variavel tem que por entre {} se não ele conta que é um comentario.
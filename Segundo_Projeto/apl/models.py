from django.db import models
from stdimage.models import StdImageField

#SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

# Create your models here.
class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2) #Casas decimais
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self): #Serve para que cada objeto criado nessa tabela, nao fique com o nome de 'Produto object' mas sim o proprio nome do produto
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs): #Função que eu quero que seja executada no sinal
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto) #Aqui to dizendo que quero que execute aquela função ANTES da tabela PRODUTO salvar algo nela
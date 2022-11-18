from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Wallet(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=50)
    slug = models.SlugField(null=True, unique=True)
    date = models.DateField(verbose_name='Data', null=True)
    hour = models.TimeField(verbose_name='Hora', auto_now_add=True, null=True)
    ballance = models.DecimalField(verbose_name='Saldo', max_digits=6, 
                                   decimal_places=2)

    class Meta:
        verbose_name  = 'Carteira'
        verbose_name_plural = 'Carteiras'

    def __str__(self):
        return self.name

    
    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.name)}-{slugify(self.date)}'
        super(Wallet, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('wallet_detail', kwargs={'slug':self.slug})


class Expense(models.Model):
    STATUS_CHOICES = (
        ('a pagar', 'A pagar'),
        ('pago', 'Pago'),
    )

    name = models.CharField(verbose_name='Nome', max_length=50)
    wallet = models.ForeignKey(Wallet, verbose_name='Carteira', null=True,
                               on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Categoria',
                                 on_delete=models.PROTECT)
    description = models.TextField(verbose_name='Descrição')
    amount = models.DecimalField(verbose_name='Valor', max_digits=6, 
                                 decimal_places=2)
    proof = models.ImageField(verbose_name='Comprovante', upload_to='uploads/',
                              blank=True)
    date_and_hour = models.DateTimeField(
        verbose_name='Data e hora',
        help_text='Use o seguinte formato: 15/06/2022 15:45'
    )
    status = models.CharField(verbose_name='Status', max_length=7,
                              choices=STATUS_CHOICES, null=True)
    

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'


    def __str__(self):
        return self.name

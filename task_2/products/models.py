from django.db import models
from django.urls import reverse

from categories.models import SubCategory


class Product(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='Название',)
    slug = models.SlugField(max_length=128,
                            unique=True,
                            verbose_name='Слаг',)
    image1 = models.ImageField(upload_to='image/product/',
                               blank=False,
                               null=False,
                               verbose_name='Картинка_1')
    image2 = models.ImageField(upload_to='image/product/',
                               blank=False,
                               null=False,
                               verbose_name='Картинка_2')
    image3 = models.ImageField(upload_to='image/product/',
                               blank=False,
                               null=False,
                               verbose_name='Картинка_3')
    price = models.PositiveIntegerField(verbose_name='Цена',)
    category = models.ForeignKey(SubCategory,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 verbose_name='Категория',
                                 related_name='product',)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('products-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

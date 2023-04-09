from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=128,
                             unique=True,
                             verbose_name='Название')
    slug = models.SlugField(max_length=128,
                            unique=True,
                            verbose_name='Слаг')
    image = models.ImageField(upload_to='image/category/',
                              verbose_name='Изображение')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class SubCategory(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='Название')
    slug = models.SlugField(max_length=128,
                            verbose_name='Слаг')
    image = models.ImageField(upload_to='image/sub_category/',
                              verbose_name='Изображение')
    parent_category = models.ForeignKey(Category,
                                        on_delete=models.CASCADE,
                                        verbose_name='Родительская категория',
                                        related_name='child')

    def __str__(self) -> str:
        return f'{self.parent_category.title} - {self.title}'

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'

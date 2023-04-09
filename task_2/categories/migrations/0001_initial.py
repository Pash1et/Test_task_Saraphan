# Generated by Django 4.1 on 2023-04-07 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='Слаг')),
                ('image', models.ImageField(upload_to='image/category/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='Слаг')),
                ('image', models.ImageField(upload_to='image/sub_category/', verbose_name='Изображение')),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='categories.category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'подкатегория',
                'verbose_name_plural': 'подкатегории',
            },
        ),
    ]

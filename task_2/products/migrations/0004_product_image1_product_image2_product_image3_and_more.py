# Generated by Django 4.1 on 2023-04-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_imageproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='image/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='image/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='image/product/'),
        ),
        migrations.DeleteModel(
            name='ImageProduct',
        ),
    ]

# Generated by Django 4.1 on 2023-04-09 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0007_remove_productinshoppingcart_unique_product_in_shoppingcart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinshoppingcart',
            name='user',
        ),
    ]

# Generated by Django 4.1 on 2023-04-09 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0006_remove_shoppingcart_products_shoppingcart_products'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='productinshoppingcart',
            name='unique_product_in_shoppingcart',
        ),
    ]

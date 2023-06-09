# Generated by Django 4.1 on 2023-04-09 12:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0014_alter_shoppingcart_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinshoppingcart',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='shoppingcart.shoppingcart'),
        ),
        migrations.AlterField(
            model_name='productinshoppingcart',
            name='quantity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from products.models import Product

User = get_user_model()


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user_cart')

    def __str__(self) -> str:
        return (f'Корзина пользователя: {self.user.username}, '
                f'стоимость: {self.total_price()}, руб.')

    def total_price(self):
        return sum(
            [product.sum()
             for product in ProductInShoppingCart.objects.filter(cart=self)]
        )

    def total_quantity(self):
        return sum(
            [product.quantity
             for product in ProductInShoppingCart.objects.filter(cart=self)]
        )

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'


class ProductInShoppingCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=(MinValueValidator(1),))
    cart = models.ForeignKey(ShoppingCart,
                             on_delete=models.CASCADE,
                             related_name='cart',)

    def __str__(self) -> str:
        return f'Стоимость: {self.product.price}'

    def sum(self):
        return self.product.price * self.quantity

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('product', 'cart'),
                name='unique_product_in_cart'
            ),
        )

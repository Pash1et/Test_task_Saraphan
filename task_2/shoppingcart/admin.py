from django.contrib import admin

from .models import ProductInShoppingCart, ShoppingCart


class ProductInShoppingCartInLine(admin.TabularInline):
    model = ProductInShoppingCart
    extra = 0


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    inlines = [ProductInShoppingCartInLine]

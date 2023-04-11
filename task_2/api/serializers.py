from rest_framework import serializers

from categories.models import Category
from products.models import Product
from shoppingcart.models import ProductInShoppingCart, ShoppingCart


class CategorySerialier(serializers.ModelSerializer):
    child_category = serializers.StringRelatedField(
        source='child',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Category
        fields = ('title', 'slug', 'image', 'child_category',)


class ProductsSerializer(serializers.ModelSerializer):
    subcategory = serializers.StringRelatedField(source='category')
    category = serializers.StringRelatedField(
        source='category.parent_category'
    )
    on_site = serializers.URLField(source='get_absolute_url',
                                   read_only=True)

    class Meta:
        model = Product
        fields = ('title', 'slug', 'category', 'subcategory',
                  'price', 'image1', 'image2', 'image3', 'on_site')


class ProductInShoppingCartSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    price = serializers.IntegerField(source='product.price')

    class Meta:
        model = ProductInShoppingCart
        fields = ('product', 'price', 'quantity', 'sum')


class ShoppingCartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    cart = ProductInShoppingCartSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = ('user', 'cart', 'total_price', 'total_quantity')


class AddProductInShoppingCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInShoppingCart
        fields = '__all__'

    def create(self, validated_data):
        quantity = validated_data.get('quantity')
        product = validated_data.get('product')
        cart = validated_data.get('cart')
        shop_cart = ProductInShoppingCart.objects.filter(cart=cart,
                                                         product=product)
        if shop_cart.exists():
            quantity = shop_cart.first().quantity + quantity
            shop_cart.update(cart=cart, quantity=quantity, product=product)
            return shop_cart.first()
        shop_cart = ProductInShoppingCart.objects.create(cart=cart,
                                                         quantity=quantity,
                                                         product=product)
        return shop_cart


class QuantityProductInShoppinCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInShoppingCart
        fields = '__all__'

    def update(self, instance, validated_data):
        quantity = validated_data.get('quantity')
        product = validated_data.get('product')
        cart = validated_data.get('cart')
        shop_cart = ProductInShoppingCart.objects.filter(cart=cart,
                                                         product=product)
        shop_cart.update(cart=cart, quantity=quantity, product=product)
        return shop_cart.first()

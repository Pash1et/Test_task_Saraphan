from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from categories.models import Category
from products.models import Product
from shoppingcart.models import ShoppingCart

from .serializers import (AddProductInShoppingCartSerializer,
                          CategorySerialier, ProductInShoppingCart,
                          ProductsSerializer,
                          QuantityProductInShoppinCartSerializer,
                          ShoppingCartSerializer)


class CategoryListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerialier
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductsListViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'

    @action(methods=('post',),
            detail=True,
            permission_classes=(IsAuthenticated,))
    def add_in_cart(self, request, slug):
        cart, bool = ShoppingCart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, slug=slug)
        quantity = request.data.get('quantity', 1)
        serializer = AddProductInShoppingCartSerializer(
            data={'product': product.pk, 'quantity': quantity, 'cart': cart.pk}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShoppingCartViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingCartSerializer
    pagination_class = None
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    @action(methods=('delete',),
            detail=False,
            url_path=('delete'),
            permission_classes=(IsAuthenticated,))
    def delete_cart(self, request):
        user = self.request.user
        cart = get_object_or_404(ShoppingCart, user=user)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=('delete',),
            detail=True,
            permission_classes=(IsAuthenticated,))
    def delete_item(self, request, pk):
        user_cart = request.user.user_cart
        product = get_object_or_404(Product, pk=pk)
        product_in_cart = get_object_or_404(ProductInShoppingCart,
                                            product=product,
                                            cart=user_cart)
        product_in_cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=('patch',),
            detail=True,
            permission_classes=(IsAuthenticated,))
    def change_quantity(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        quantity = request.data.get('quantity', 1)
        cart = get_object_or_404(ShoppingCart, user=request.user)
        serializer = QuantityProductInShoppinCartSerializer(
            ProductInShoppingCart,
            data={'product': product.pk, 'cart': cart.pk, 'quantity': quantity}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

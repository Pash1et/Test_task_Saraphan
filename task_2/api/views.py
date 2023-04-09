
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)

from products.models import Product
from shoppingcart.models import ShoppingCart
from .serializers import (AddProductInShoppingCart, CategorySerialier,
                          ShoppingCartSerializer, ProductsSerializer)
from categories.models import Category


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
        serializer = AddProductInShoppingCart(
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

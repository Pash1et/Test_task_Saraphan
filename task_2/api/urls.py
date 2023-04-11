from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (CategoryListViewSet, ProductsListViewset,
                    ShoppingCartViewSet)

router = DefaultRouter()

router.register('categories', CategoryListViewSet, basename='categories')
router.register('products', ProductsListViewset, basename='products')
router.register('cart', ShoppingCartViewSet, basename='cart')


urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]

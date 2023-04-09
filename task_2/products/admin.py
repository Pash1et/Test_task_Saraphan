from django.contrib import admin
from .models import Product


#class ImageProductInline(admin.TabularInline):
#    model = ImageProduct
#    min_num = 3
#    max_num = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price')
    prepopulated_fields = ({'slug': ('title',)})
    #inlines = [ImageProductInline]

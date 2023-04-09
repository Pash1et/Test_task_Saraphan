from django.contrib import admin
from .models import Category, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    prepopulated_fields = ({'slug': ('title',)})


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent_category',)
    prepopulated_fields = ({'slug': ('title',)})

from django.contrib import admin
from .models import Category, Tag, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_available', 'created_at')
    list_filter = ('category', 'tags', 'is_available')
    search_fields = ('name', 'description')
    filter_horizontal = ('tags',)

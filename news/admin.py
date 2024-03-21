from django.contrib import admin
from .models import Product, ProductAttribute, Category, ProductImage, Tag
from django.utils.safestring import mark_safe

class ProductAttributeTabularInline(admin.TabularInline):
    model = ProductAttribute

class ProductImageTabularInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_filter = ('category', 'tags')
    readonly_fields = ('get_full_image',)
    filter_horizontal = ('tags',)
    inlines = [ProductAttributeTabularInline, ProductImageTabularInline]

    @admin.display(description='Изображение')
    def get_image(self, product: Product):
        return mark_safe(f'<img src="{product.image.url}" width="150px">')

    @admin.display(description='Изображение')
    def get_full_image(self, product: Product):
        return mark_safe(f'<img src="{product.image.url}" width="50%">')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


from django.contrib import admin
from .models import Category, Product, Slide
from django.utils.html import format_html




# категории продуктов
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # Автоматически заполняет slug из поля name
    prepopulated_fields = {'slug': ('name',)}

# Продукты
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available'] # Можно менять цену прямо в списке!
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ("preview", "order", "active")
    list_editable = ("order", "active")

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="120" />', obj.image.url)
        return "-"



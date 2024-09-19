from django.contrib import admin
from django.utils.html import format_html
from .models import Products, Order

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'discount_price', 'category','description', 'image_preview')
    search_fields = ('title', 'category', 'description')
    list_filter = ('category',)
    list_editable = ('price', 'discount_price')
    ordering = ('id',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image)
    image_preview.short_description = 'Image Preview'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'city', 'state', 'total')
    search_fields = ('name', 'email', 'city', 'state')
    list_filter = ('state',)
    ordering = ('id',)
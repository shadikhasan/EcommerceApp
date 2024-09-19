from django.contrib import admin
from .models import Products, Order

# Register your models here.

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'category')  # Columns to display in the admin list view
    search_fields = ('title', 'category')  # Search functionality
    list_filter = ('category',)  # Filter by category

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'state', 'total')  # Columns to display in the admin list view
    search_fields = ('name', 'email', 'city')  # Search functionality
    list_filter = ('state',)  # Filter by state

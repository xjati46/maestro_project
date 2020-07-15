from django.contrib import admin
from admin_app.models import Product, Order


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'student', 'coach', 'arsip')

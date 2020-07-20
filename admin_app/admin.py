from django.contrib import admin
from admin_app.models import Product, Order
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'student', 'coach', 'arsip')
    list_filter = ('coach', 'arsip')

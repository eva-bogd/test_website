from django.contrib import admin

from .models import Category, Service, Order


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'executor', 'price')
    list_editable = ('name', 'category', 'executor', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'executor')
    empty_value_display = '-пусто-'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'customer', 'executor', 'price', 'status')
    list_filter = ('customer', 'executor')
    search_fields = ('name', 'customer')
    empty_value_display = '-пусто-'


admin.site.register(Category)

from django.contrib import admin

from products.models import Clothing, Perfum, Ring

@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'colour', 'size', 'price', 'stock')
@admin.register(Perfum)
class PerfumAdmin(admin.ModelAdmin):
    list_display = ('name', 'smell', 'price', 'stock')
@admin.register(Ring)
class RingAdmin(admin.ModelAdmin):
    list_display = ('name', 'material', 'weight', 'price', 'stock')

# Register your models here.

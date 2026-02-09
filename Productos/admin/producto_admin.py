from django.contrib import admin

from Productos.models import Productos


@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "categoria")
    list_filter = ("nombre",)
    search_fields = ("nombre",)
    list_per_page = 25
    readonly_fields = ("slug",)
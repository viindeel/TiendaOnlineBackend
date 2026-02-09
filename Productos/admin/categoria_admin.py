from django.contrib import admin

from Productos.models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "slug")
    list_filter = ("nombre",)
    search_fields = ("nombre",)
    list_per_page = 25
    readonly_fields = ("slug",)
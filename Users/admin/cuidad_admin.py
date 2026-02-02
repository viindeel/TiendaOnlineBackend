from django.contrib import admin

from Users.models import CiudadModel



@admin.register(CiudadModel)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    ordering = ('-name',)
    readonly_fields = ('slug',)
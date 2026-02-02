from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from Users.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ("email", "username", "role__name" ,  "is_active", "is_staff" ,"is_superuser")
    # list_filter = ("email", "username", "is_active", "is_staff" ,"is_superuser")
    # search_fields = ("email")
    # ordering = ("-email")

    # # fieldsets = (
    # # ("Inicio de Sesión", {
    # "classes": ("wide",),
    # # "fields": ("email", "password", "first_name")}),
    # ("Inicio de Sesión", {
    #     # "classes": ("wide",),
    #     # # "fields": ("username", "password", "first_name")}),
    # # )
admin.site.register(User, CustomUserAdmin)

from django.contrib import admin

from Users.models import Role


@admin.register(Role)
class RolesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active",)
    list_filter = ("is_active",)
    readonly_fields = ("slug",)

    fieldsets = (
        ("Informacion del rol", {
            "classes": ("wide",),
            "fields" : ("name", "slug", "is_active",),
        }),
    )


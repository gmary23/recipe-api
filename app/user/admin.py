from django.contrib import admin
from user import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"] # ordenados por id, a medida pelo que for criado
    list_display = ["email", "name"] # campos que aparecem na lista
    readonly_fields = ["last_login"] # o registro do último login - não pode ser editado, pois é registrado pelo sistema

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (("Personal Info"), {"fields": ("name",)}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (("Important dates"), {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

# Register your models here.
admin.site.register(models.User, UserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ("-created_at",)
    list_display = ("email",)
    list_filter = ("is_staff", "is_superuser", "is_active")

    fieldsets = (
        (
            None,
            {
                "fields": ("email",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "groups",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": ("email",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "groups",
                )
            },
        ),
    )


admin.site.register(User, UserAdmin)

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import User
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    ordering = ("-created_at",)
    list_display = ("email",)
    list_filter = ("is_staff", "is_superuser", "is_active")

    fieldsets = (
        (
            None,
            {
                "fields": ("password",),
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
                "fields": ("email", "password1", "password2"),
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

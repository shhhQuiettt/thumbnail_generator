from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserChangeForm as BaseUserChangeForm,
    UserCreationForm as BaseUserCreationForm,
    ReadOnlyPasswordHashField,
)
from django import forms


class UserChangeForm(BaseUserChangeForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ["is_staff", "is_superuser"]
        # exclude = ["email"]


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = "__all__"

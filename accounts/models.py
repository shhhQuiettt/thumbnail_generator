from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class Tier(models.Model):
    name = models.CharField(max_length=50, unique=True)
    allowed_height = models.IntegerField(
        "Allowed image height in px", null=True, blank=True
    )
    can_get_original_link = models.BooleanField(
        "Permission to fetch an original image link", default=False
    )


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", False)
        other_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)

        if other_fields.get("is_staff") == False:
            raise ValueError("super user must have is_staff=True")
        if other_fields.get("is_superuser") == False:
            raise ValueError("super user must have is_superuser=True")

        return self._create_user(email, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tier = models.ForeignKey(Tier, null=True, blank=True, on_delete=models.RESTRICT)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ()

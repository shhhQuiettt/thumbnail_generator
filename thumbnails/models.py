from django.db import models
from django.conf import settings
import os
from pathlib import Path

# Create your models here.


def _get_original_image_path(image_instance, filename) -> str:
    # e.g. if users pk is 123 and original is named kitty.png,
    # it returns "user_123/kitty/original.png"
    base_filename, ext = os.path.splitext(filename)
    return os.path.join(
        f"user_{image_instance.owner.pk}", base_filename, "original" + ext
    )


class Image(models.Model):
    img = models.ImageField(upload_to=_get_original_image_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


def _get_thumbnail_image_path(thumbnail_instance, filename) -> str:
    # e.g. if original image path is "user_123/kitty/original.png"
    # and thumbnail size is 200 function returns
    # user_123/kitty/200px.png
    ext = os.path.split(filename)[-1]
    return os.path.join(
        Path(thumbnail_instance.original_img.img.path).parent,
        thumbnail_instance.size.height + "px" + ext,
    )


class ThumbnailSize(models.Model):
    height = models.IntegerField()


class Thumbnail(models.Model):
    img = models.ImageField(upload_to=_get_thumbnail_image_path)
    size = models.ForeignKey(ThumbnailSize, on_delete=models.RESTRICT)
    original_img = models.ForeignKey(Image, null=True, on_delete=models.SET_NULL)

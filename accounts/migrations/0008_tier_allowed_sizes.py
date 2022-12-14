# Generated by Django 4.1.1 on 2022-09-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0002_remove_image_owner'),
        ('accounts', '0007_remove_tier_allowed_width_tier_can_get_original_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='tier',
            name='allowed_sizes',
            field=models.ManyToManyField(related_name='tiers', to='thumbnails.thumbnailsize'),
        ),
    ]

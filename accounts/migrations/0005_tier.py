# Generated by Django 4.1.1 on 2022-09-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('allowed_width', models.IntegerField(blank=True, null=True, verbose_name='Allowed thumbnail width in px')),
                ('allowed_height', models.IntegerField(blank=True, null=True, verbose_name='Allowed image height in px')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-29 17:26

import catalogo.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categoria',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=catalogo.models.get_file_path),
        ),
        migrations.AddField(
            model_name='categoria',
            name='trending',
            field=models.BooleanField(default=False, help_text='0=default , 1=trending', null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_original',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to=catalogo.models.get_file_path),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-24 13:46

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='venue',
        ),
        migrations.AddField(
            model_name='photo',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main_app.event'),
            preserve_default=False,
        ),
    ]

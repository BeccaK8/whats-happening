# Generated by Django 5.0.1 on 2024-01-24 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_photo_venue_photo_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.event'),
        ),
    ]

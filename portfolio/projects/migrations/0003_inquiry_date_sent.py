# Generated by Django 5.1.1 on 2024-09-07 03:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_inquiry_date_sent_inquiry_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='date_sent',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.3 on 2025-02-04 04:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_visitor_visit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='visit_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Время визита'),
        ),
    ]

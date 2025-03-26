# Generated by Django 5.1.3 on 2025-02-03 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('organization', models.CharField(max_length=100, verbose_name='Организация')),
                ('recipient', models.CharField(max_length=100, verbose_name='Цель визита')),
                ('visit_date', models.DateField(verbose_name='Дата посещения')),
            ],
        ),
    ]

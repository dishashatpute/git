# Generated by Django 5.0.6 on 2024-05-14 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('melodyapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='composition',
        ),
        migrations.RemoveField(
            model_name='product',
            name='prodapp',
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0002_storage'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='is_tested',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 5.1.1 on 2024-09-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.BooleanField()),
                ('blood_group', models.CharField(max_length=50)),
                ('identity_document_type', models.CharField(max_length=50)),
                ('identity_document_number', models.IntegerField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
        ),
    ]

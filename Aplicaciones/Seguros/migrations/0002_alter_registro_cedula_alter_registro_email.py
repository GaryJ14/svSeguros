# Generated by Django 5.1 on 2024-08-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seguros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='cedula',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registro',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]

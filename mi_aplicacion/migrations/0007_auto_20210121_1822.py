# Generated by Django 3.1.5 on 2021-01-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0006_auto_20210121_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='prestado',
            field=models.BooleanField(default=False),
        ),
    ]

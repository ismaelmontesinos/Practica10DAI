# Generated by Django 3.1.5 on 2021-01-21 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0008_auto_20210121_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
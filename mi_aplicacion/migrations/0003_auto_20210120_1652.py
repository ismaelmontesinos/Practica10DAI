# Generated by Django 3.1.5 on 2021-01-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0002_auto_20210120_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='publicacion',
            field=models.DateField(),
        ),
    ]

# Generated by Django 2.0.8 on 2018-12-12 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_lei', '0003_auto_20181212_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetolei',
            name='projeto',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='projetolei',
            name='protocolo',
            field=models.IntegerField(unique=True),
        ),
    ]
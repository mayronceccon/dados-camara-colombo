# Generated by Django 2.0.8 on 2018-11-24 16:14

from django.db import migrations, models
import vereador.models


class Migration(migrations.Migration):

    dependencies = [
        ('vereador', '0003_auto_20181124_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vereador',
            name='foto',
            field=models.ImageField(
                blank=True, null=True, upload_to=vereador.models.content_file_name),
        ),
    ]

# Generated by Django 2.0.8 on 2018-11-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vereador', '0002_auto_20181124_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vereador',
            name='foto',
            field=models.ImageField(
                blank=True, null=True, upload_to='vereador/%Y/%m/%d/'),
        ),
    ]

# Generated by Django 3.0 on 2019-12-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bairro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bairro',
            options={'verbose_name': 'bairro', 'verbose_name_plural': 'bairros'},
        ),
        migrations.AlterField(
            model_name='bairro',
            name='identificacao',
            field=models.CharField(max_length=150, unique=True, verbose_name='Identificação'),
        ),
    ]
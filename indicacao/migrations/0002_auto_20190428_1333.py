# Generated by Django 2.2 on 2019-04-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pauta', '0007_pauta_indicacao_exportada'),
        ('indicacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicacao',
            name='numero',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='indicacao',
            unique_together={('numero', 'pauta')},
        ),
    ]
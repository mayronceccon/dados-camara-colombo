# Generated by Django 2.2 on 2019-04-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pauta', '0006_auto_20181216_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='pauta',
            name='indicacao_exportada',
            field=models.BooleanField(
                default=False, verbose_name='Indicacoes Exportadas'),
        ),
    ]

# Generated by Django 2.0.8 on 2018-12-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vereador_link', '0002_auto_20181212_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vereadorlink',
            name='tipo',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT, to='tipo_solicitacao.TipoSolicitacao'),
        ),
        migrations.AlterField(
            model_name='vereadorlink',
            name='vereador',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT, to='vereador.Vereador'),
        ),
    ]

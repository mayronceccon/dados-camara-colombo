# Generated by Django 2.2 on 2019-04-28 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicacao', '0002_auto_20190428_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicacao',
            name='vereador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='indicacoes', to='vereador.Vereador'),
        ),
    ]

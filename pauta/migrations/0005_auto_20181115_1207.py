# Generated by Django 2.0.8 on 2018-11-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pauta', '0004_auto_20181113_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pauta',
            name='cadastro',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

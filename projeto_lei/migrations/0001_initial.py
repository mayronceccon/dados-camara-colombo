# Generated by Django 2.0.8 on 2018-12-12 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vereador', '0004_auto_20181124_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetoLei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.IntegerField()),
                ('protocolo', models.IntegerField()),
                ('assunto', models.TextField()),
                ('observacao', models.TextField()),
                ('data_divulgacao', models.DateField(blank=True, null=True)),
                ('data_aprovacao', models.DateField(blank=True, null=True)),
                ('data_arquivamento', models.DateField(blank=True, null=True)),
                ('vereador', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='vereador.Vereador')),
            ],
        ),
    ]
# Generated by Django 2.0.8 on 2018-11-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vereador',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('apelido', models.CharField(blank=True, max_length=100, null=True)),
                ('data_nascimento', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefone_gabinete', models.CharField(
                    blank=True, max_length=20, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('foto', models.ImageField(
                    blank=True, null=True, upload_to='vereador')),
                ('cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

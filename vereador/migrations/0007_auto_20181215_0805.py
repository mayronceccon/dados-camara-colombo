# Generated by Django 2.0.8 on 2018-12-15 10:05

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vereador', '0006_vereador_anos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vereador',
            name='anos',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), (
                '2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018')], max_length=119),
        ),
    ]

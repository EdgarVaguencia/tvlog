# Generated by Django 3.2.15 on 2022-10-28 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capitulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporada',
            name='serie',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='temporada',
            name='serie_id',
            field=models.IntegerField(default=0),
        ),
    ]

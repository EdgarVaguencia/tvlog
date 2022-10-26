# Generated by Django 3.2.15 on 2022-10-26 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='capitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_lanzamiento', models.DateTimeField()),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False)),
                ('fecha_eliminado', models.DateTimeField(blank=True, null=True)),
                ('temporada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='capitulos', to='capitulos.temporada')),
            ],
        ),
    ]

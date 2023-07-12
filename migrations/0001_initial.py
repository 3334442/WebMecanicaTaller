# Generated by Django 4.2.1 on 2023-07-02 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('nombre', models.CharField(max_length=70, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('idTrabajo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('foto', models.ImageField(default='fotos/noImg.png', null=True, upload_to='fotos')),
                ('descripcion', models.TextField(max_length=1000)),
                ('categoria', models.ForeignKey(default='nuevo', on_delete=django.db.models.deletion.CASCADE, to='MecanicaAutomotora.categoria')),
                ('mecanico', models.ForeignKey(default='nuevo', on_delete=django.db.models.deletion.CASCADE, to='MecanicaAutomotora.mecanico')),
            ],
        ),
    ]

# Generated by Django 2.2.10 on 2020-07-21 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ensurance', '0002_auto_20200721_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aseguradora', models.CharField(max_length=100)),
                ('poliza', models.CharField(max_length=30)),
                ('plan', models.CharField(max_length=20)),
                ('legajo', models.CharField(max_length=30)),
                ('titular', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=20)),
                ('tipodoc', models.CharField(max_length=20)),
                ('fechanacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('montoasegurado', models.FloatField()),
                ('fechainicio', models.DateField()),
                ('coberturaadicional', models.CharField(max_length=100)),
                ('beneficiarios', models.CharField(max_length=3)),
                ('pregunta1', models.BooleanField()),
                ('pregunta2', models.BooleanField()),
            ],
            options={
                'db_table': 'planilla',
            },
        ),
    ]

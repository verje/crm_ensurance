# Generated by Django 2.2.10 on 2020-07-22 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ensurance', '0003_planilla'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planilla',
            name='coberturaadicional',
        ),
        migrations.RemoveField(
            model_name='planilla',
            name='plan',
        ),
        migrations.AddField(
            model_name='planilla',
            name='cobertura1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='planilla',
            name='cobertura2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='planilla',
            name='cobertura3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='planilla',
            name='plan1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='planilla',
            name='plan2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='planilla',
            name='plan3',
            field=models.BooleanField(default=False),
        ),
    ]

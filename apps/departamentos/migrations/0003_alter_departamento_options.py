# Generated by Django 3.2.9 on 2021-12-07 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0002_alter_departamento_short_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': ''},
        ),
    ]

# Generated by Django 3.2 on 2024-11-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0011_delete_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

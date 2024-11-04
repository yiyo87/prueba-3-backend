# Generated by Django 3.2 on 2024-11-02 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0008_alter_partido_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='equipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partidos', to='equipos.equipo'),
        ),
    ]

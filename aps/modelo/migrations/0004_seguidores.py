# Generated by Django 2.2.6 on 2019-11-26 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0003_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguidores',
            fields=[
                ('Seg_id', models.AutoField(primary_key=True, serialize=False)),
                ('aceptado', models.BooleanField(default=True)),
                ('seguido_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguido', to='modelo.User')),
                ('seguidor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguidor', to='modelo.User')),
            ],
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-26 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0006_notificaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('msj_id', models.AutoField(primary_key=True, serialize=False)),
                ('mensaje', models.CharField(max_length=100)),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to='modelo.User')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='modelo.User')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]

# Generated by Django 2.2.6 on 2020-02-27 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0010_user_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fecha_nacimiento',
        ),
    ]

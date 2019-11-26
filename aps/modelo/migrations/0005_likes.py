# Generated by Django 2.2.6 on 2019-11-26 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0004_seguidores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.User')),
            ],
        ),
    ]
# Generated by Django 2.2.6 on 2020-01-03 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0008_auto_20191126_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AlterField(
            model_name='seguidores',
            name='aceptado',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.User')),
            ],
        ),
    ]
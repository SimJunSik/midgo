# Generated by Django 2.1.4 on 2019-04-09 20:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('midgo_app', '0005_auto_20190409_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='check_notification',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

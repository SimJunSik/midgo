# Generated by Django 2.1.4 on 2019-04-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midgo_app', '0004_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='category',
            field=models.CharField(choices=[('reply', 'Reply'), ('notice', 'Notice')], max_length=30, null=True),
        ),
    ]

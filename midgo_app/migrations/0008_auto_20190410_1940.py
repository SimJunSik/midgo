# Generated by Django 2.1.4 on 2019-04-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midgo_app', '0007_auto_20190410_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleimage',
            name='file',
            field=models.ImageField(upload_to='articleImage/'),
        ),
    ]

# Generated by Django 2.1.4 on 2019-04-04 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('midgo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=20)),
                ('age', models.CharField(default='0', max_length=10)),
                ('breed', models.CharField(default='unknown', max_length=50)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

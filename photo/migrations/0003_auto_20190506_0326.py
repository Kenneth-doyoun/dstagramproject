# Generated by Django 2.2 on 2019-05-06 03:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20190504_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite_post', to=settings.AUTH_USER_MODEL),
        ),
    ]

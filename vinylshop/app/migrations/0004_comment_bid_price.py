# Generated by Django 3.1.4 on 2020-12-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_album_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='bid_price',
            field=models.FloatField(default=0),
        ),
    ]
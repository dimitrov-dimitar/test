# Generated by Django 3.1.4 on 2020-12-12 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_comment_bid_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='bid_price',
            field=models.FloatField(default=None),
        ),
    ]
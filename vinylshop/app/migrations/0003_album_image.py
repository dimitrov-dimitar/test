# Generated by Django 3.1.4 on 2020-12-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201212_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]

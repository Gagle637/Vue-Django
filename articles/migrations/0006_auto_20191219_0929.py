# Generated by Django 3.0.1 on 2019-12-19 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20191219_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='detect',
            field=models.CharField(default='alert alert-light text-secondary', max_length=500),
        ),
    ]

# Generated by Django 3.0.1 on 2019-12-19 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20191218_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='detect',
            field=models.CharField(default='MouseOut', max_length=10),
        ),
    ]

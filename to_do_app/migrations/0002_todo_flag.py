# Generated by Django 3.0.6 on 2020-05-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]
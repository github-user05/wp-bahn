# Generated by Django 2.2.6 on 2019-12-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bahn', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segment',
            old_name='ende',
            new_name='ziel',
        ),
        migrations.AlterField(
            model_name='verbindung',
            name='favorit',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-06 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_devicelog_checkinconditiondevice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicelog',
            name='checkinYear',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devicelog',
            name='checkoutYear',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

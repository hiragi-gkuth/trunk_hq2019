# Generated by Django 2.1.7 on 2019-03-17 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oapi', '0004_auto_20190317_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularity',
            name='scan_count',
            field=models.IntegerField(default=1),
        ),
    ]

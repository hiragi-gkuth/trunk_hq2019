# Generated by Django 2.1.7 on 2019-03-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oapi', '0003_product_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularity',
            name='scan_count',
            field=models.IntegerField(default=0),
        ),
    ]

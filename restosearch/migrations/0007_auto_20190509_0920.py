# Generated by Django 2.2.1 on 2019-05-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restosearch', '0006_restaurant_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='city',
            field=models.CharField(max_length=500),
        ),
    ]

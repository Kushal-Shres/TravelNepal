# Generated by Django 2.2 on 2019-05-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='Contact',
            field=models.IntegerField(default=0),
        ),
    ]

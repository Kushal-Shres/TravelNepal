# Generated by Django 2.2 on 2019-05-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0016_auto_20190503_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='Place image'),
        ),
    ]

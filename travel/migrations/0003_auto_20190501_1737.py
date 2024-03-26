# Generated by Django 2.2 on 2019-05-01 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20190501_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='type',
        ),
        migrations.AddField(
            model_name='place',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='travel.Category'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2 on 2019-05-02 05:41

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0012_auto_20190501_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='location',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tourist',
            name='email',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tourist',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=17),
        ),
    ]

# Generated by Django 2.0.2 on 2018-09-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20180906_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image_url',
            field=models.URLField(default='', max_length=250),
        ),
    ]
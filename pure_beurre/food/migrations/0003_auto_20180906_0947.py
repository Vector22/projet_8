# Generated by Django 2.0.2 on 2018-09-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20180730_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='image',
        ),
        migrations.RemoveField(
            model_name='food',
            name='imageSmall',
        ),
        migrations.AddField(
            model_name='food',
            name='image_url',
            field=models.URLField(default='https://static.openfoodfacts.org/images/products/871/814/457/0908/front_fr.6.400.jpg', max_length=250),
            preserve_default=False,
        ),
    ]
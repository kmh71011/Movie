# Generated by Django 3.0.8 on 2020-07-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200705_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]

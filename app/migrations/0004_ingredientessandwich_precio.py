# Generated by Django 3.2.5 on 2021-07-18 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_sandwich_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientessandwich',
            name='precio',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

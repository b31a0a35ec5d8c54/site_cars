# Generated by Django 2.0.7 on 2018-07-21 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_auto_20180721_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
    ]
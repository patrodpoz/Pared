# Generated by Django 2.2.4 on 2021-04-29 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pared', '0003_auto_20210428_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=64),
        ),
    ]

# Generated by Django 2.2.4 on 2021-04-29 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pared', '0002_auto_20210428_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]

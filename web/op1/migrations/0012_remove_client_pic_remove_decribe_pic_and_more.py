# Generated by Django 4.1.3 on 2022-12-24 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('op1', '0011_client_pic_decribe_pic_municipality_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='decribe',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='municipality',
            name='pic',
        ),
    ]
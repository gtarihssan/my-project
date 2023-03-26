# Generated by Django 4.1.3 on 2023-01-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op1', '0018_municipality_locali'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipality',
            name='finance',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='municipality',
            name='gouve',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='municipality',
            name='plani',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op1', '0007_rename_decribe_comment_decribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decribe',
            name='text',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
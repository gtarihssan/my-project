# Generated by Django 4.1.3 on 2022-12-23 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('op1', '0008_alter_decribe_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='op1.client'),
        ),
    ]

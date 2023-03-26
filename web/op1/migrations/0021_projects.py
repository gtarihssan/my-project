# Generated by Django 4.1.3 on 2023-01-06 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('op1', '0020_decribe_admin_decribe_decribe_tach_alter_client_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='')),
                ('decription', models.CharField(blank=True, max_length=2000, null=True)),
                ('date_de_debut', models.DateField(auto_now=True)),
                ('municipilty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='op1.municipality')),
            ],
        ),
    ]
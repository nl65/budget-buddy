# Generated by Django 4.1.5 on 2023-01-06 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(choices=[('Work', 'Work'), ('Other', 'Other')], default='Work', max_length=25),
        ),
    ]
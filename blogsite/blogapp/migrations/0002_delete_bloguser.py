# Generated by Django 4.0.4 on 2022-08-22 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogUser',
        ),
    ]
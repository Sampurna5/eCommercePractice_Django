# Generated by Django 3.1.6 on 2021-02-26 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210226_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='test',
        ),
    ]

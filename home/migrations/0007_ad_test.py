# Generated by Django 3.1.6 on 2021-02-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_ad_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='test',
            field=models.TextField(blank=True),
        ),
    ]
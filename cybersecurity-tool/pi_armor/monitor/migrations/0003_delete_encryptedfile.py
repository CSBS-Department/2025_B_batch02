# Generated by Django 4.2.7 on 2024-04-08 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_encryptedfile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EncryptedFile',
        ),
    ]
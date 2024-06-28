# Generated by Django 5.0 on 2024-01-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack_type', models.CharField(choices=[('DDoS', 'DDoS'), ('PortScan', 'Port Scanning')], max_length=100)),
                ('attacker_ip', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField()),
            ],
        ),
    ]
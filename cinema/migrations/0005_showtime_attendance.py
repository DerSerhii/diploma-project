# Generated by Django 4.0.6 on 2022-08-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_alter_spectator_wallet_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='showtime',
            name='attendance',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Attendance'),
        ),
    ]

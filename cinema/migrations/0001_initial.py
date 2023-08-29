# Generated by Django 4.0.6 on 2023-08-23 12:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='film title')),
                ('duration', models.DurationField(verbose_name='duration')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('release_year', models.PositiveSmallIntegerField(verbose_name='release day')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('starring', models.CharField(max_length=255, verbose_name='starring')),
                ('director', models.CharField(max_length=50, verbose_name='director')),
                ('poster', models.ImageField(null=True, upload_to='poster/%Y/%m/%d/', verbose_name='poster')),
            ],
            options={
                'verbose_name': 'film',
                'verbose_name_plural': 'films',
                'db_table': 'films',
                'ordering': ['release_year', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ScreenHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='hall name')),
                ('capacity', models.PositiveSmallIntegerField(verbose_name='capacity')),
            ],
            options={
                'verbose_name': 'screen hall',
                'verbose_name_plural': 'screen halls',
                'db_table': 'screen_halls',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='the film start')),
                ('end', models.DateTimeField(verbose_name='the film end')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='ticket price')),
                ('attendance', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'showtime',
                'verbose_name_plural': 'showtimes',
                'db_table': 'showtimes',
                'ordering': ['start'],
            },
        ),
        migrations.CreateModel(
            name='SpectatorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='account')),
            ],
            options={
                'verbose_name': 'spectator profile',
                'verbose_name_plural': 'spectator profiles',
                'db_table': 'spectator_profiles',
                'ordering': ['user__username'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='quantity')),
                ('purchase_time', models.DateTimeField(auto_now_add=True)),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tickets', to='cinema.showtime')),
            ],
            options={
                'verbose_name': 'ticket',
                'verbose_name_plural': 'tickets',
                'db_table': 'tickets',
                'ordering': ['-purchase_time'],
            },
        ),
    ]

# Generated by Django 2.2.3 on 2019-10-23 23:35

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0060_auto_20191023_1430'),
        ('economy', '0001_initial'),
        ('marketing', '0006_manualstat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenAirdrop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('num_uses_total', models.IntegerField()),
                ('num_uses_remaining', models.IntegerField()),
                ('current_uses', models.IntegerField(default=0)),
                ('secret', models.CharField(max_length=255, unique=True)),
                ('comments', models.CharField(blank=True, max_length=255)),
                ('sender_pk', models.CharField(blank=True, max_length=255)),
                ('sender_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airdrops', to='dashboard.Profile')),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airdrops', to='economy.Token')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

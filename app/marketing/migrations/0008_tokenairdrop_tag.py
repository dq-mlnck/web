# Generated by Django 2.2.3 on 2019-10-23 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0007_tokenairdrop'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokenairdrop',
            name='tag',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

# Generated by Django 2.2.4 on 2019-11-05 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0061_hackathonproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathonevent',
            name='show_results',
            field=models.BooleanField(default=True, help_text='Hide/Show the links to access hackathon results'),
        ),
    ]

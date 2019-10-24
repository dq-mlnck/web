# Generated by Django 2.2.3 on 2019-10-23 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0008_tokenairdrop_tag'),
        ('quests', '0016_auto_20191023_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='reward_token',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quests_reward_token', to='marketing.TokenAirdrop'),
        ),
    ]

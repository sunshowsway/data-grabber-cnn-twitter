# Generated by Django 2.0 on 2019-11-10 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_scrapyitem_tweet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quote',
        ),
        migrations.AddField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

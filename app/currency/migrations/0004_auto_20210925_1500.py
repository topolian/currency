# Generated by Django 3.2.5 on 2021-09-25 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email_from',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(max_length=2056),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
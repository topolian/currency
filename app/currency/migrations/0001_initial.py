# Generated by Django 3.2.5 on 2021-07-22 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=120)),
                ('message', models.TextField()),
            ],
        ),
    ]

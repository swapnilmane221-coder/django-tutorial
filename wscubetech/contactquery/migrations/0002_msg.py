# Generated by Django 5.1.2 on 2025-03-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactquery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
    ]

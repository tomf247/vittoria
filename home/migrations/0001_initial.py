# Generated by Django 4.1.4 on 2023-01-18 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emails', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
    ]

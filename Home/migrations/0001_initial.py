# Generated by Django 4.2.5 on 2023-10-01 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

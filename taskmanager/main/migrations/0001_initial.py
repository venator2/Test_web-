# Generated by Django 4.0.1 on 2022-01-16 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdentificationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='')),
                ('last_name', models.CharField(max_length=50, verbose_name='')),
                ('email', models.CharField(max_length=70, verbose_name='')),
            ],
        ),
    ]

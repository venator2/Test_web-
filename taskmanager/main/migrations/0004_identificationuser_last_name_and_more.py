# Generated by Django 4.0.1 on 2022-01-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_identificationuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='identificationuser',
            name='last_name',
            field=models.CharField(default='', max_length=50, verbose_name='Прізвище'),
        ),
        migrations.AlterField(
            model_name='identificationuser',
            name='first_name',
            field=models.CharField(default='', max_length=50, verbose_name='Імя'),
        ),
        migrations.AlterField(
            model_name='identificationuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

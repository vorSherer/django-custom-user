# Generated by Django 3.1.1 on 2020-09-03 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='notes_field',
            field=models.CharField(default='', max_length=60),
        ),
    ]
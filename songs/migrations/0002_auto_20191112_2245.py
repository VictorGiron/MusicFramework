# Generated by Django 2.2.7 on 2019-11-12 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.TimeField(),
        ),
    ]
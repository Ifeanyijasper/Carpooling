# Generated by Django 3.2 on 2021-05-27 11:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0014_alter_rating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='passenger',
            field=models.CharField(default='ifeanyi', max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='username',
            field=models.CharField(default='ifeanyi', max_length=225),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2 on 2021-04-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0009_alter_feedback_question4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='question5',
            field=models.IntegerField(choices=[(1, 'Very Unlikey'), (2, 'Unlikely'), (3, 'Neutral'), (4, 'likely'), (5, 'Very Likely')]),
        ),
    ]
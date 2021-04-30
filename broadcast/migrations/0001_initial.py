# Generated by Django 3.2 on 2021-04-25 12:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='broadcast date')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='time')),
                ('send_to_all', models.BooleanField(default=False, verbose_name='send to all')),
                ('bc_time', models.TimeField(default=django.utils.timezone.now, verbose_name='rebc time')),
                ('bc_date', models.DateField(default=django.utils.timezone.now, verbose_name='rebc date')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comment')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='date')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='time')),
            ],
        ),
        migrations.CreateModel(
            name='DirectionBroadcast',
            fields=[
                ('broadcast_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='broadcast.broadcast')),
                ('location', models.TextField(verbose_name='current Location')),
                ('destination', models.TextField(verbose_name='destination')),
                ('additional_info', models.TextField(verbose_name='additional information')),
            ],
            bases=('broadcast.broadcast',),
        ),
        migrations.CreateModel(
            name='ImageBroadcast',
            fields=[
                ('broadcast_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='broadcast.broadcast')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
            bases=('broadcast.broadcast',),
        ),
        migrations.CreateModel(
            name='RideBroadcast',
            fields=[
                ('broadcast_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='broadcast.broadcast')),
                ('source', models.CharField(max_length=256, verbose_name='source')),
                ('dest', models.CharField(max_length=256, verbose_name='destination')),
                ('date_needed', models.DateField(default=django.utils.timezone.now, verbose_name='date needed')),
            ],
            bases=('broadcast.broadcast',),
        ),
        migrations.CreateModel(
            name='TextBroadcast',
            fields=[
                ('broadcast_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='broadcast.broadcast')),
                ('message', models.TextField()),
            ],
            bases=('broadcast.broadcast',),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='date')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='time')),
                ('broadcast_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='broadcast_like', to='broadcast.broadcast')),
            ],
        ),
    ]
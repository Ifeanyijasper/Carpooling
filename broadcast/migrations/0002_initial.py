# Generated by Django 3.2 on 2021-04-25 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('broadcast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='liker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='broadcast_message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='broadcast_comment', to='broadcast.broadcast'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='broadcast',
            name='bc_from',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bcfrom', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='broadcast',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='broadcast_broadcast_related', to=settings.AUTH_USER_MODEL),
        ),
    ]
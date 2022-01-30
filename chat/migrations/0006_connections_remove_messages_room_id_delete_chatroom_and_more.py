# Generated by Django 4.0.1 on 2022-01-30 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_alter_chatroom_room_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=32, unique=True)),
                ('friend', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='friend', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='messages',
            name='room_id',
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
        migrations.AddField(
            model_name='messages',
            name='connection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.connections'),
        ),
    ]

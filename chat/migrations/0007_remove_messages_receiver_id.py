# Generated by Django 4.0.1 on 2022-02-06 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_connections_remove_messages_room_id_delete_chatroom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='receiver_id',
        ),
    ]

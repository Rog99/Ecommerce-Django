from django.db import models

# Create your models here.


class Connections(models.Model):
    room_id = models.CharField(max_length=32, blank=False, null=False, unique=True)
    user = models.ForeignKey('authentication.CustomUser', on_delete=models.SET_NULL, related_name='user', null=True)
    friend = models.ForeignKey('authentication.CustomUser', on_delete=models.SET_NULL, related_name='friend', null=True)


class Messages(models.Model):
    sender_id = models.ForeignKey('authentication.CustomUser', on_delete=models.SET_NULL, blank=True, null=True,
                                  related_name='senders'
                                  )
    connection = models.ForeignKey(Connections, on_delete=models.SET_NULL, blank=True, null=True)
    message = models.TextField(null=False, blank=False)

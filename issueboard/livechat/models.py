from django.db import models


class ChatRoom(models.Model):
    room = models.CharField(max_length=100, default='anonymous')
    create_time = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.room

class ChatBoard(models.Model):
    room = models.CharField(max_length=100, default='anonymous')
    name = models.CharField(max_length=100, default='anonymous')
    message = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.room

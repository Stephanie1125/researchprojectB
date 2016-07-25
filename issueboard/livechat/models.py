from django.db import models


class ChatBoard(models.Model):
    name = models.CharField(max_length=100, default='anonymous')
    message = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)


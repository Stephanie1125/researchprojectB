
from django.db import models


class IssuePost(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_created=True, auto_now_add=True)
    def __str__(self):
        return self.title
    def get_content(self):
        return self.title + " " + self.content
    def get_time(self):
        return self.create_time

class IssueChat(models.Model):
    issue_title = models.CharField(max_length = 100)
    name = models.CharField(max_length=100, default='anonymous')
    message = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.issue_title
    def get_content(self):
        return self.message

    def get_time(self):
        return self.create_at

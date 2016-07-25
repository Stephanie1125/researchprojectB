from django.contrib import admin
from .models import IssuePost

class IssueBoardAdmin(admin.ModelAdmin):
    list_display = ('title','name', 'email', 'content', 'create_time')

admin.site.register(IssuePost, IssueBoardAdmin)
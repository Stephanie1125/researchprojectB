from django.contrib import admin
from .models import IssuePost, IssueChat

class IssueBoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'email', 'content', 'create_time')

admin.site.register(IssuePost, IssueBoardAdmin)

class IssueChatAdmin(admin.ModelAdmin):
    list_display = ('issue_title','name', 'message', 'create_at')

admin.site.register(IssueChat, IssueChatAdmin)
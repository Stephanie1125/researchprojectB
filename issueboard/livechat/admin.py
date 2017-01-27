from django.contrib import admin
from .models import ChatBoard


class ChatBoardAdmin(admin.ModelAdmin):
    list_display = ('room', 'name', 'message', 'create_at')


admin.site.register(ChatBoard, ChatBoardAdmin)

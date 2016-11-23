from django.contrib import admin
from .models import ChatBoard, ChatRoom


class ChatBoardAdmin(admin.ModelAdmin):
    list_display = ('room', 'name', 'message', 'create_at')


admin.site.register(ChatBoard, ChatBoardAdmin)


class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('room', 'create_time')

admin.site.register(ChatRoom, ChatRoomAdmin)

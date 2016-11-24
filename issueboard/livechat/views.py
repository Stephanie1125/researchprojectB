
from django.shortcuts import render, redirect
from .models import ChatBoard, ChatRoom
from django import forms
from issue.views import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

def livechat(request, roomname):
    form = MessageForm(request.POST or None)
    message_list = ChatBoard.objects.all().order_by('pk')
    if request.user.is_authenticated():
        room_id = roomname + ' chatroom'
        message_list = message_list.filter(
            Q(room__icontains=room_id)).distinct()

    return render(request, 'livechat.html', {'message_list': message_list, 'form': form, 'roomname':roomname})


class MessageForm(forms.Form):
    message = forms.CharField(max_length=200)

    def clean(self, *args, **kwargs):
        message = self.cleaned_data.get("message")

        if not message:
            raise forms.ValidationError("Please input your message.")

        return super(MessageForm, self).clean(*args, **kwargs)


def create_chat(request, username):
    if request.method == 'POST':
        f = MessageForm(request.POST or None)
        if f.is_valid():
            message = f.cleaned_data['message']
            if request.user.is_authenticated():
                room = username + ' chatroom'
                name = request.user.username
                save_message = ChatBoard()
                save_message.room = room
                save_message.name = name
                save_message.message = message
                save_message.save()
                return redirect(reverse('livechat', args=(username,)))

        return redirect(reverse('livechat', args=(username,)))



@staff_member_required
def chatroom_admin(request):
    message_room_list = ChatBoard.objects.all().order_by('-create_at')
    rooms = []
    added_username = set()
    for user in User.objects.all():
        if user.is_staff:
            added_username.add(user.username)


    for message in message_room_list:
        if message.name in added_username:
            continue
        added_username.add(message.name)
        rooms.append(message)

    return render(request, 'chatroom.html', {
        'rooms': rooms,
    })
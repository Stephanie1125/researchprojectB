
from django.shortcuts import render, redirect
from .models import ChatBoard
from django import forms


def livechat(request):
    message_list = ChatBoard.objects.all().order_by('pk')
    return render(request, 'livechat.html', {'message_list': message_list})


class MessageForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(max_length=200)


def chat_submit(request):
    if request.method == 'POST':
        f = MessageForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            message = f.cleaned_data['message']
        else:
            return livechat(request)

    save_message = ChatBoard()
    save_message.name = name
    save_message.message = message
    save_message.save()
    return redirect(r'http://127.0.0.1:8000/livechat')

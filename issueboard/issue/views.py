from django.shortcuts import render, redirect
from .models import IssuePost, IssueChat
from django import forms
from django.core.urlresolvers import reverse


def home(request):
    issue_list = IssuePost.objects.all().order_by('pk')
    return render(request, 'home.html', {
        'issue_list': issue_list,
    })


def issue_detail(request, pk):
    issue = IssuePost.objects.get(pk=pk)
    issue_chat_list = IssueChat.objects.all().order_by('pk')
    return render(request, 'issue.html', {
        'issue': issue,
        'issue_chat_list': issue_chat_list,
    })


class IssueForm(forms.Form):
    title = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    content = forms.CharField(max_length = 1000)


def add_issue(request):
    issue_list = IssuePost.objects.all()
    return render(request, 'newissue.html', {
        'issue_list': issue_list,
    })


def issue_submit(request):
    if request.method == 'POST':
        f = IssueForm(request.POST)
        if f.is_valid():
            title = f.cleaned_data['title']
            name = f.cleaned_data['name']
            email = f.cleaned_data['email']
            content = f.cleaned_data['content']
        else:
            return home(request)

    save_issuepost = IssuePost()
    save_issuepost.title = title
    save_issuepost.name = name
    save_issuepost.email = email
    save_issuepost.content = content
    save_issuepost.save()
    return redirect(r'http://127.0.0.1:8000/home')


class IssueChatForm(forms.Form):
    issue_title = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)


def issue_chat_submit(request, pk):
    if request.method == 'POST':
        f = IssueChatForm(request.POST)
        if f.is_valid():
            issue_title = f.cleaned_data['issue_title']
            name = f.cleaned_data['name']
            message = f.cleaned_data['message']
        else:
            return issue_detail(request)

    save_message = IssueChat()
    save_message.issue_title = issue_title
    save_message.name = name
    save_message.message = message
    save_message.save()
    return redirect(reverse('issue_detail', args=(pk,)))





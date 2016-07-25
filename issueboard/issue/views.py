from django.shortcuts import render, redirect
from .models import IssuePost
from django import forms


def home(request):
    issue_list = IssuePost.objects.all().order_by('-pk')
    return render(request, 'home.html', {
        'issue_list': issue_list,
    })


def issue_detail(request, pk):
    issue = IssuePost.objects.get(pk=pk)
    return render(request, 'issue.html', {
        'issue': issue,
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
from django.shortcuts import render, redirect
from .models import IssuePost, IssueChat
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, get_user_model, login, logout
from .user_forms import UserLoginForm, UserRegisterForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    issue_list = IssuePost.objects.all().order_by('pk')
    query = request.GET.get("q")
    if query:
        issue_list = issue_list.filter(title__icontains=query)
    paginator = Paginator(issue_list, 10)
    page = request.GET.get('page')
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        issues = paginator.page(1)
    except EmptyPage:
        issues = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {
        'issues': issues,
    })


def user_login(request):
    form = UserLoginForm(request.POST or None)
    title = 'User login'
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/home")
    return render(request, 'form.html', {'form': form, 'title': title})


def user_logout(request):
    logout(request)
    return redirect("/home")

def user_register(request):
    title = "User Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password = password)
        login(request, new_user)
        return redirect("/home")

    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'form.html', context)


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





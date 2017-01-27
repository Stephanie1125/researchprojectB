import os
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import IssuePost, IssueChat
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from .user_forms import UserLoginForm, UserRegisterForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def initial(request):
    return redirect("/home")

@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html', {'username': request.user.username})

@login_required(login_url='/login')
def about(request):
    return render(request, 'about.html', {'username': request.user.username})

@login_required(login_url='/login')
def contact(request):
    return render(request, 'contact.html', {'username': request.user.username})


@login_required(login_url='/login')
def home_issuepost(request):
    issue_list = IssuePost.objects.all().order_by('-create_time')
    query = request.GET.get("q")
    if query:
        issue_list = issue_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)).distinct()

    paginator = Paginator(issue_list, 10)
    page = request.GET.get('page')
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        issues = paginator.page(1)
    except EmptyPage:
        issues = paginator.page(paginator.num_pages)
    return render(request, 'issue_post.html', {
        'issues': issues,
        'username': request.user.username
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
    return render(request, 'login_form.html', {'form': form, 'title': title})


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
        new_user = authenticate(username=user.username, password= password)
        login(request, new_user)
        return redirect("/home")

    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'register_form.html', context)


@login_required(login_url='/login')
def issue_detail(request, pk):
    issue = IssuePost.objects.get(pk=pk)
    issue_chat_list = IssueChat.objects.all().order_by('pk')
    return render(request, 'issue.html', {
        'issue': issue,
        'issue_chat_list': issue_chat_list,
        'username': request.user.username,
    })


class IssueForm(forms.Form):
    title = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    content = forms.CharField(max_length=1000)

    def clean(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        content = self.cleaned_data.get("content")

        if not title or not content or not name or not email:
            raise forms.ValidationError("Please input all the fields.")

        return super(IssueForm, self).clean(*args, **kwargs)


@login_required(login_url='/login')
def add_issue(request):
    issue_list = IssuePost.objects.all()
    form = IssueForm(request.POST or None)
    return render(request, 'newissue.html', {
        'issue_list': issue_list,
        'form': form,
        'username': request.user.username
    })


@login_required(login_url='/login')
def issue_submit(request):
    if request.method == 'POST':
        f = IssueForm(request.POST or None)
        if f.is_valid():
            title = f.cleaned_data.get('title')
            name = f.cleaned_data.get('name')
            email = f.cleaned_data.get('email')
            content = f.cleaned_data.get('content')

            save_issuepost = IssuePost()
            save_issuepost.title = title
            save_issuepost.name = name
            save_issuepost.email = email
            save_issuepost.content = content
            save_issuepost.save()

            return redirect('/issuepost')

        context = {
            'form': f,
            'username': request.user.username,
        }
        return render(request, 'newissue.html', context)


class IssueChatForm(forms.Form):
    issue_title = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)


@login_required(login_url='/login')
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


@staff_member_required
def export(request):
    def write_to_file(post, chat_list, output_path):
        outputfile = os.path.join(output_path, str(post.id))
        contents = [post]
        contents += [c for c in chat_list]

        with open(outputfile, "w") as fout:
            for item in contents:
                fout.write("\t".join([item.name, item.get_content(), str(item.get_time())]) + "\n")

    path = os.path.join(os.path.expanduser("~"), "issuepost_export")
    if not os.path.exists(path):
        os.mkdir(path)
    post_dict = {post.title:post for post in IssuePost.objects.all()}
    chat_list = IssueChat.objects.all()
    dialogues = {}

    for chat in chat_list:
        the_post = post_dict[chat.issue_title]
        dialogues.setdefault(the_post, [])
        dialogues[the_post].append(chat)

    for post, chat_list in dialogues.items():
        write_to_file(post, chat_list, path)

    return redirect('/issuepost')

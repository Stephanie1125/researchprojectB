from django.conf.urls import include, url
from django.contrib import admin
from issue.views import home, add_issue, issue_submit, issue_detail, issue_chat_submit, user_login, user_logout, user_register
#issue_chat_detail
from livechat.views import livechat, chat_submit
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', user_login, name='login'),
    url(r'^logout/', user_logout, name='logout'),
    url(r'^register/', user_register, name='register'),
    url(r'^newissue$', add_issue, name = 'add_issue'),
    url(r'^api/issue_submit$', issue_submit, name='issue_submit'),
    url(r'^issue/(?P<pk>\d+)/$', issue_detail, name='issue_detail'),
    url(r'^livechat$', livechat, name='livechat'),
    url(r'^api/chat_submit$', chat_submit, name='chat_submit'),
    url(r'^api/issue_chat_submit/(?P<pk>\d+)$', issue_chat_submit, name='issue_chat_submit'),
    url(r'^home$', home, name='home'),
]
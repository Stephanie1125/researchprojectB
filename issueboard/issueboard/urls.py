from django.conf.urls import include, url
from django.contrib import admin
from issue.views import home, add_issue, issue_submit, issue_detail, issue_chat_submit
#issue_chat_detail
from livechat.views import livechat, chat_submit
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', home, name = 'home'),
    url(r'^newissue$', add_issue, name = 'add_issue'),
    url(r'^api/issue_submit$', issue_submit, name='issue_submit'),
    url(r'^issue/(?P<pk>\d+)/$', issue_detail, name='issue_detail'),
    url(r'^livechat$', livechat, name='livechat'),
    url(r'^api/chat_submit$', chat_submit, name='chat_submit'),
    # url(r'^issue/(?P<pk>\d+)/$', issue_chat_detail, name='issue_chat_detail'),
    url(r'^api/issue_chat_submit$', issue_chat_submit, name='issue_chat_submit'),

]
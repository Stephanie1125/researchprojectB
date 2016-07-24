from django.conf.urls import include, url
from django.contrib import admin
from chat.views import home, post_detail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
]

from django.conf.urls import url
from django.contrib import admin


from landing.api.views import (
    PostCreateAPIView,
    PostDeleteAPIView,
    PostDetailAPIView,
    PostListAPIView,
    PostUpdateAPIView,
    )


app_name="myproject"
## 
urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='real_home'),
    # url(r'^home$', post_home, name='home'),
    # url(r'^blog$', post_list, name='list'),
    # url(r'^about$', post_about, name='about'),
    # url(r'^contact$', post_contact, name='contact'),
    url(r'^create/$', PostCreateAPIView.as_view(), name = 'create'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
    # url(r'^tag/(?P<tag>[a-zA-Z0-9_-]+)/$', search_by_tag, name='search'),
]

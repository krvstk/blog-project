from django.conf.urls import url


from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    post_about,
    post_contact,
    post_home,
    search_by_tag,
    real_home,
)
app_name="myproject"
## 
urlpatterns = [
    url(r'^$', real_home, name='real_home'),
    url(r'^home$', post_home, name='home'),
    url(r'^blog/$', post_list, name='list'),
    url(r'^about$', post_about, name='about'),
    url(r'^contact$', post_contact, name='contact'),
    url(r'^create/$', post_create),
    url(r'^blog/(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^blog/(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^blog/(?P<slug>[\w-]+)/delete/$', post_delete),
    url(r'^tag/(?P<tag>[a-zA-Z0-9_-]+)/$', search_by_tag, name='search'),
]

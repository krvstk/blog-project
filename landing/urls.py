from django.conf.urls import url


from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    post_about,
    post_contact,
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^about/$', post_about, name='about'),
    url(r'^contact/$', post_contact, name='contact'),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),

    #   url(r'^(?P<slug>[\w-]+)/contact/$', post_contact),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

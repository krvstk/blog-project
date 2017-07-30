#from django.contrib import admin
#from .models import *


# class ClientAdmin (admin.ModelAdmin):
#    list_display = ["name", "email"]


# class Meta:
#    model = Client
#admin.site.register(Client, ClientAdmin)

from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)

from urllib.parse import quote
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Post


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        form.save_m2m()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.publish > timezone.now().date() or instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote(instance.content)

    tags = instance.tags.names()
    slug_tags = instance.tags.slugs()

    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
        "tags": tags,
        "slug_tags": slug_tags,
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    
    today = timezone.now().date()
    queryset_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 2)  # Show 10 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)


    context = {
        "object_list": queryset,
        "title": "Blog",
        "page_request_var": page_request_var,
        "today": today,
    }
    if request.is_ajax():
        return render(request, "post_list.html", context)
    else:  
        return render(request, "post_list_extended.html", context)

def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item Saved")
        form.save_m2m()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:list")


def post_about(request):
    if request.is_ajax():
        return render(request, "about.html")
    else:
        context = {
            "title": "About me",
        }
        return render(request, "about_extended.html", context)


def post_contact(request):
    if request.is_ajax():
        return render(request, "contact.html")
    else:
        context = {
            "title": "Contact",
        }
        return render(request, "contact_extended.html", context)

def real_home(request):
    context = {
        "title": "Home",
    }
    return render(request, "home_extended.html", context)


def post_home(request):
    if request.is_ajax():
        return render(request, "home.html")
    else:
        context = {
            "title": "Home",
        }
        return render(request, "home_extended.html", context)


def search_by_tag(request, tag):
    posts_with_tag = Post.objects.filter(tags__slug__in=[tag])
    context = {
        "title": "Search By Tag",
        "posts_with_tag": posts_with_tag
    }
    return render(request, "tags.html", context)


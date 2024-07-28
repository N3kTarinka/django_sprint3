from blog.models import Category, Post
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .constants import POSTS_BY_PAGE


def index(request):
    posts = Post.objects.filter(is_published=True, category__is_published=True,
                                pub_date__lte=timezone.now()
                                ).select_related('author',
                                                 'category')[:POSTS_BY_PAGE]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.filter(is_published=True, category__is_published=True,
                            pub_date__lte=timezone.now()
                            ).select_related('author', 'category'), id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    posts = Post.objects.filter(is_published=True, category__is_published=True,
                                pub_date__lte=timezone.now(), category=category
                                ).select_related('author', 'category')
    context = {'category': category.title, 'post_list': posts}
    return render(request, 'blog/category.html', context)

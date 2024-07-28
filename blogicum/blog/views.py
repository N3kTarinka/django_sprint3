from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post
from .constants import POSTS_BY_PAGE


def get_published_posts():
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).select_related('author', 'category')


def index(request):
    posts = get_published_posts()[:POSTS_BY_PAGE]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(get_published_posts(), id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    posts = get_published_posts().filter(category=category)
    context = {'category': category.title, 'post_list': posts}
    return render(request, 'blog/category.html', context)

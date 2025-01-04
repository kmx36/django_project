from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Post, Category


def filter_posts(posts):
    return posts.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    return render(request, 'blog/index.html', {
        'posts': filter_posts(Post.objects.all())[:5]
    })


def post_detail(request, post_id):
    return render(request, 'blog/detail.html', {
        'post': get_object_or_404(filter_posts(Post.objects.all()), pk=post_id)
    })


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects,
        slug=category_slug,
        is_published=True
    )
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': filter_posts(category.post.all()),
    })

from django.shortcuts import render
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 3
    template_name = 'blog/index.html'


class PostDetailView(generic.DetailView):
    model = Post


def get_posts_by_category(request, category_name):
    post_list = Post.objects.filter(category__name__iexact=category_name)
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context)


def get_posts_by_keyword(request):
    search_key = request.GET['q']
    post_list = Post.objects.filter(title__icontains=search_key)
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context)

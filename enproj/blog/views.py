from django.db.models import Count
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .forms import PostForm
from .models import blogpost, blogcategories
from django.views import View


def blog(request):
    posts = blogpost.objects.filter(status=True).all().order_by('created_date').reverse()
    categories = blogcategories.objects.all().annotate(post_count=Count('blogpost'))
    return render(request, 'site/bloglist.html', {
        'posts': posts,
        'categories': categories,
    })


def post(request, slug):
    data = get_object_or_404(blogpost, pk=slug)
    categories = blogcategories.objects.all().annotate(post_count=Count('blogpost'))
    return render(request, 'site/post-details.html', {
        'data': data,
        'categories': categories,
    })


class category(View):
    def get(self, request, slug):
        categoryposts = blogpost.objects.filter(status=True, category__slug=slug)
        categories = blogcategories.objects.all().annotate(post_count=Count('blogpost'))
        return render(request, 'site/categorylist.html', {
            'categoryposts': categoryposts,
            'categories': categories,
        }
                      )


def newpost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
        return redirect('/')
    else:
        form = PostForm()
    return render(request, 'site/post-edit.html',
                  {'form': form})

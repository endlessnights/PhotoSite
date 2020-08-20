from django.shortcuts import render

# Create your views here.
from .models import blogpost


def blog(request):
    posts = blogpost.objects.filter(status=True).all()
    return render(request, 'site/bloglist.html', {
        'posts': posts,
    })
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import GalleryForm, CategoryForm, ImageForm
from .models import post, categories, subcategory
from django.views import View


class showportfolios(View):
    def get(self, request):
        getportfolios = categories.objects.all().order_by('order').annotate(posts_count=Count('category'))
        return render(request, 'site/portfolios.html', {
            'getportfolios': getportfolios,
        }
                      )


class category(View):
    def get(self, request, getpfcategory):
        showposts = subcategory.objects.annotate(posts_count=Count('subcategory')).filter(category__slug=getpfcategory)
        return render(request, 'site/categories.html', {
            'showposts': showposts,
        }
                      )


class showposts(View):
    def get(self, request, getpfcategory, getsubcategory):
        showpics = post.objects.filter(category__slug=getsubcategory)
        return render(request, 'site/pics.html', {
            'showpics': showpics,
        }
                      )


def newgallery(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
        return redirect('/')
    else:
        form = GalleryForm()
    return render(request, 'site/gallery-edit.html',
                  {'form': form})


def newcategory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
        return redirect('/')
    else:
        form = CategoryForm()
    return render(request, 'site/gallery-category-edit.html',
                  {'form': form})


def newimage(request, getpfcategory, getsubcategory):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.category = getsubcategory
            post.save()
        return redirect('http://127.0.0.1:8000/gallery/travel/rome/')
    else:
        form = ImageForm()
    return render(request, 'site/gallery-upload-images.html',
                  {'form': form})

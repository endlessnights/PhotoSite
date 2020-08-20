from django.db.models import Count
from django.shortcuts import render
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
        showposts = subcategory.objects.annotate(posts_count=Count('posts')).filter(category__slug=getpfcategory)
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

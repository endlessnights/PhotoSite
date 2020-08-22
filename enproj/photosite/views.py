from django.shortcuts import render
from .models import post
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView
from django.urls import reverse


def home(request):
    posts = post.objects.filter(status=True)
    return render(request, 'site/home.html',
                  {'posts': posts,
                   }
                  )


class gallery(View):
    def get(self, request, getcategory):
        showcategory = post.objects.filter(category__slug=getcategory)
        return render(request, 'site/gallery.html', {
            'showcategory': showcategory,
        }
                      )

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/<int:slug>/', views.post, name='post'),
    path('tinymce/', include('tinymce.urls')),
    path('blog/add/', views.newpost, name='newpost'),
    url(r'blog/cat/(?P<slug>[a-zA-Z0-9]+)/$', views.category.as_view(), name='category'),
]

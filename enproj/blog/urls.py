from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

urlpatterns = [
    path('blog/', views.blog, name='blog'),
]

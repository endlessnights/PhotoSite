from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'gallery/$', views.showportfolios.as_view(), name='showportfolios'),
    url(r'gallery/(?P<getpfcategory>[a-zA-Z0-9]+)/$', views.category.as_view(), name='category'),
    url(r'gallery/(?P<getpfcategory>[a-zA-Z0-9]+)/(?P<getsubcategory>[a-zA-Z0-9]+)/$', views.showposts.as_view(), name='showposts'),
    url(r'gallery/(?P<getpfcategory>[a-zA-Z0-9]+)/(?P<getsubcategory>[a-zA-Z0-9]+)/edit/', views.newimage, name='newimage'),
    path('gallery-edit/', views.newgallery, name='newgallery'),
    path('gallery-category-edit/', views.newcategory, name='newcategory'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#   site.ru/travel/monaco/

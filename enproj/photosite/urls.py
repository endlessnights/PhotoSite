from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

urlpatterns = [
                  path('', views.home, name='home'),
                  url(r'files/(?P<getcategory>[a-zA-Z0-9]+)/$', views.gallery.as_view(),
                      name='gallery'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

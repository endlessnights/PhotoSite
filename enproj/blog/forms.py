from django import forms

from .models import blogpost, blogcategories
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    class Meta:
        model = blogpost
        fields = ('slug',
                  'name',
                  'category',
                  'description',
                  'desc',
                  'cover',
                  'videolink',
                  'status',
                  )

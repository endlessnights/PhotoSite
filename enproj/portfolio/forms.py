from django import forms

from .models import categories, subcategory, post


class GalleryForm(forms.ModelForm):
    class Meta:
        model = categories
        fields = ('slug',
                  'name',
                  'description',
                  'cover',
                  'status',
                  )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = subcategory
        fields = ('slug',
                  'name',
                  'description',
                  'cover',
                  'category',
                  'gmap',
                  'coords',
                  'status',
                  )

class ImageForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('slug',
                  'name',
                  'description',
                  'category',
                  'image',
                  'videolink',
                  'status',
                  )
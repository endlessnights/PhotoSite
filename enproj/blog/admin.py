from django.contrib import admin

# Register your models here.
from .models import blogpost, blogcategories


@admin.register(blogcategories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'slug',
        'name',
        'description',
        'cover',
    ]


@admin.register(blogpost)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'slug',
        'author',
        'name',
        'description',
        'cover',
        'videolink',
        'created_date',
        'status',
        'category',
    ]

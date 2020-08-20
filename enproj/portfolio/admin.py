from django.contrib import admin

from .models import categories, post, subcategory


@admin.register(categories)
class PublishAdmin(admin.ModelAdmin):
    list_display = [
        'slug',
        'name',
        'description',
        'cover',
    ]


@admin.register(subcategory)
class SubcatAdmin(admin.ModelAdmin):
    list_display = [
        'slug',
        'category',
        'name',
        'description',
        'cover',
    ]


@admin.register(post)
class PublishAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'status',
        'name',
        'image',
        'created_date',
    ]

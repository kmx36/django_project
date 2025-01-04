from django.contrib import admin

from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'is_published',
        'created_at',
        'title',
        'description',
        'slug',
    )
    search_fields = (
        'title',
        'description',
        'slug',
    )
    list_filter = (
        'is_published',
    )
    list_display_links = (
        'title',
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'is_published',
        'created_at',
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'is_published',
    )
    list_display_links = (
        'name',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'is_published',
        'created_at',
        'title',
        'text',
        'pub_date',
        'author'
    )
    search_fields = (
        'title',
        'text',
    )
    list_filter = (
        'is_published',
        'author',
        'location',
        'category',
    )
    list_display_links = (
        'title',
    )


admin.site.register(Category, CategoryAdmin)

admin.site.register(Location, LocationAdmin)

admin.site.register(Post, PostAdmin)

admin.site.empty_value_display = 'Не задано'

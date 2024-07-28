from blog.models import Category, Location, Post
from django.contrib import admin

from .constants import REPRESENTATION_LENGTH

admin.site.empty_value_display = 'Не задано'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    list_editable = ('slug', 'is_published')
    list_display_links = ('title',)
    list_per_page = REPRESENTATION_LENGTH


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('name',)
    list_per_page = REPRESENTATION_LENGTH


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',
                    'location', 'pub_date', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'author',
                     'location', 'category')
    list_filter = ('is_published', 'author',
                   'location', 'category', 'pub_date')
    list_display_links = ('title',)
    list_per_page = REPRESENTATION_LENGTH


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)

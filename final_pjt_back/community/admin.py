from django.contrib import admin
from .models import Comment, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'content', 'created_at', 'updated_at']
    list_display_links = ['id']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content', 'created_at', 'updated_at']
    list_display_links = ['id']


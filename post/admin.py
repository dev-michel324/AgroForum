from django.contrib import admin

from .models import Categorys, Post, Comment

# Register your models here.
# admin.site.register(Categorys)
# admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']

admin.site.register(Post, PostAdmin)

@admin.register(Categorys)
class CategorysAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created']
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'user', 'post']



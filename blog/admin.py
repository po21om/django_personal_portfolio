from django.contrib import admin

from blog.models import Category, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    def __str__(self) -> str:
        return self.name

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'creation_date', 'modification_date']
    list_display_links = ['id', 'title']
    list_filter = ['categories']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'author', 'creation_date']
    list_display_links = ['id', 'post']
    list_filter = ['post']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

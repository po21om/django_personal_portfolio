from django.contrib import admin

from blog.models import Category, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    def __str__(self) -> str:
        return self.name

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'creation_date', 'modification_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'author', 'creation_date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

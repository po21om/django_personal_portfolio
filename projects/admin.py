from django.contrib import admin

from projects.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


admin.site.register(Project, ProjectAdmin)
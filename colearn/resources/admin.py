from django.contrib import admin
from resources.models import Resource, Tag

# Register your models here.

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_by', 'created_at']
    search_fields = ['title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


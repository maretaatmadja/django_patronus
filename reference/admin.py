from django.contrib import admin
from .models import Reference

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'author', 'created', 'updated')
    list_filter = ('title', 'description', 'link', 'author', 'created', 'updated')
    search_fields = ('title', 'description')
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ('created',)
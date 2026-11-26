
from django.contrib import admin
from .models import Category, Job


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'category', 'location', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'location')

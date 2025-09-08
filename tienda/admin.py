from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "available")
    list_filter = ("available",)
    search_fields = ("title", "author")

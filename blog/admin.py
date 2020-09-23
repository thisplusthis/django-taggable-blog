# blog/admin.py

from django.contrib import admin

from .models import BlogEntry, Image

admin.register(Image)


class InlineImage(admin.TabularInline):
    model = Image


@admin.register(BlogEntry)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [InlineImage]


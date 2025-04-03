from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)  # to make slug read only filed
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Book, BookAdmin)

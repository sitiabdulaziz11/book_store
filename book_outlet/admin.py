from django.contrib import admin

from .models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)  # to make slug read only filed
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating", "author",)
    list_display = ("title", "author")

admin.site.register(Book, BookAdmin)
admin.site.register(Author)

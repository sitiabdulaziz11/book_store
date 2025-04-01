from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Book

# Create your views here.

def index(request):
    """base page
    """
    book = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": book
    })

def book_detail(request, id):
    """Views which gives detail of the book.
    """
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, pk=id)   # this is alternative of above try and except part
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })
    

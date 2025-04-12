from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg

from .models import Book

# Create your views here.

def index(request):
    """base page
    """
    # book = Book.objects.all()
    # book = Book.objects.all().order_by("-rating")  # - is for rating desendeing order
    book = Book.objects.all().order_by("title")
    num_books = book.count()
    avg_rating = book.aggregate(Avg("rating"))  # rating__avg,
    
    return render(request, "book_outlet/index.html", {
        "books": book,
        "total_number_of_books": num_books,
        "average_rating": avg_rating
    })

# def book_detail(request, id):
def book_detail(request, slug):
    """Views which gives detail of the book.
    """
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    # book = get_object_or_404(Book, pk=id)   # this is alternative of above try and except part
    book = get_object_or_404(Book, slug=slug)   # this is alternative of above try and except part
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })

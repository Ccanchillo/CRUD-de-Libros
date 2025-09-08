from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from .models import Book


@require_http_methods(["GET", "POST"])
def books_list(request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        published_date = request.POST.get('published_date') or None

        if title and author:
            book = Book(title=title, author=author)
            if published_date:
                try:
                    book.published_date = published_date
                except Exception:
                    pass
            book.save()
        return redirect('books_list')

    books = Book.objects.all()
    return render(request, 'tienda/books.html', { 'books': books })


@require_http_methods(["POST"])
def toggle_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.available = not book.available
    book.save()
    return redirect('books_list')


@require_http_methods(["POST"])
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('books_list')


@require_http_methods(["GET", "POST"])
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        published_date = request.POST.get('published_date') or None
        available = True if request.POST.get('available') == 'on' else False

        if title and author:
            book.title = title
            book.author = author
            book.available = available
            book.published_date = published_date or None
            try:
                # If invalid date, leave as-is
                book.save()
            except Exception:
                book.save()
        return redirect('books_list')

    return render(request, 'tienda/book_edit.html', { 'book': book })

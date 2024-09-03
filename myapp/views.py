from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

@login_required
def book_list(request):
    books = Book.objects.filter(owner=request.user)
    return render(request, 'myapp/book_list.html', {'books': books})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk, owner=request.user)

    # Injecting a 404 error
    if book.title == "Not Found":
        raise Http404("Book not found for testing purposes")

    return render(request, 'myapp/book_detail.html', {'book': book})

@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user

            # Injecting an error
            if book.title == "Error":
                raise ValueError("Intentional Error for Testing")

            # Injecting a validation error
            if request.POST.get('title') == "Invalid":
                form.add_error('title', "This title is intentionally invalid")

            if form.is_valid():
                book = form.save(commit=False)
                book.owner = request.user
                book.save()
                return redirect('book_list')

    else:
        form = BookForm()
    return render(request, 'myapp/book_form.html', {'form': form})

@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'myapp/book_form.html', {'form': form})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'myapp/book_confirm_delete.html', {'book': book})
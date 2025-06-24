
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import Book
from django.urls import reverse_lazy


# craete book
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_date']
    template_name = 'book_cbv/book_form.html'
    success_url = reverse_lazy('book-list')


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book_cbv/book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_cbv/book_detail.html'
    context_object_name = 'book' # default is 'object'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_cbv/book_edit.html'
    fields = ['title','author','description']
    success_url = reverse_lazy('book-list')
    context_object_name = 'book'





class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_cbv/book_confirm_delete.html'
    success_url = reverse_lazy('books:book-list')
    context_object_name = 'book'


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from regularExam.author.forms import AuthorCreateForm, AuthorDeleteForm, AuthorEditForm
from regularExam.author.models import Author
from regularExam.utils import get_author_obj


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_author_obj()
        return super().form_valid(form)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/details-author.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_posts'] = self.object.post_set.count()
        context['last_post'] = self.object.post_set.last()

        return context

    def get_object(self, queryset=None):
        return get_author_obj()


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_author_obj()


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_author_obj()

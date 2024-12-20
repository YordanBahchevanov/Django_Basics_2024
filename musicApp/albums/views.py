from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from albums.models import Album
from musicApp.utils import get_user_obj


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


# def create_album(request):
#     form = AlbumCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             album = form.save(commit=False)
#             album.owner = get_user_obj()
#             album.save()
#             return redirect('home')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'albums/album-add.html', context)


class AlbumDetailsView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-details.html'


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    pk_url_kwarg = 'id'
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('home')


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
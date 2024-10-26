from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from musicApp.utils import get_user_obj


class ProfileDetailView(DetailView):
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()


# def profile_detail_view(request):
#     user = get_user_obj()
#     context = {
#         'user': user,
#     }
#     return render(request, 'profiles/profile-details.html', context)


class ProfileDeleteView(DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()


# def profile_delete_view(request):
#     user = get_user_obj()
#
#     if request.method == 'POST':
#         user.delete()
#         return redirect('home')
#
#     context = {
#         'user': user,
#     }
#
#     return render(request, 'profiles/profile-delete.html', context)
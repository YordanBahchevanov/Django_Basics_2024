from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from regularExam.posts.models import Post
from regularExam.utils import get_author_obj


class IndexView(TemplateView):
    template_name = 'common/index.html'


class DashboardView(ListView):
    model = Post
    template_name = 'common/dashboard.html'
    context_object_name = 'posts'

    def get_queryset(self):

        return Post.objects.all()



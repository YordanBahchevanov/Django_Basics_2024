from django.urls import path

from regularExam.author import views

urlpatterns = [
    path('create/', views.AuthorCreateView.as_view(), name='author-create'),
    path('details/', views.AuthorDetailView.as_view(), name='author-details'),
    path('edit/', views.AuthorEditView.as_view(), name='author-edit'),
    path('delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
]
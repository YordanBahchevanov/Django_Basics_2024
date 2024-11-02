from django.urls import path, include

from regularExam.posts import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', include([
        path('details/', views.PostDetailsView.as_view(), name='post-details'),
        path('edit/', views.PostEditView.as_view(), name='edit-post'),
        path('delete/', views.PostDeleteView.as_view(), name='delete-post'),
    ]))
]
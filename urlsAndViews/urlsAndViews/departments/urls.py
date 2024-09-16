from django.urls import path

from urlsAndViews.departments import views
from urlsAndViews.departments.views import index

urlpatterns = [
    path('', index),
    path('<int:pk>/', views.view_with_int_pk),
    path('<variable>/', views.view_with_name),
]
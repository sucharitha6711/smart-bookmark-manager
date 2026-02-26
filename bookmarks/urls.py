from django.urls import path
from . import views

urlpatterns = [
    path('',              views.index,           name='index'),
    path('api/bookmarks/',     views.bookmark_list,   name='bookmark-list'),
    path('api/bookmarks/<int:pk>/', views.bookmark_detail, name='bookmark-detail'),
]
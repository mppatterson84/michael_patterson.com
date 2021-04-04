from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostListAllView,
    PostSearchView,
    CategoryListView,
    CategoryCreateView,
    CategoryDeleteView,
    CategoryFilterView,
)

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/new/', PostCreateView.as_view(), name='post-new'),
    path('blog/<slug:slug>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('blog/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('blog/search/', PostSearchView.as_view(), name='blog-search'),
    path('blog/all/', PostListAllView.as_view(), name='post-list-all'),
    path('blog/categories/', CategoryListView.as_view(), name='category-list'),
    path('blog/categories/new/', CategoryCreateView.as_view(), name='category-new'),
    path('blog/categories/<slug:slug>/delete/',
         CategoryDeleteView.as_view(), name='category-delete'),
    path('blog/categories/filter/',
         CategoryFilterView.as_view(), name='category-filter'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]

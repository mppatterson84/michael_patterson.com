from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostListAllView,
    PostSearchView,
    CategoryListView,
    CategoryFilterView,
)

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/search/', PostSearchView.as_view(), name='blog-search'),
    path('blog/all/', PostListAllView.as_view(), name='post-list-all'),
    path('blog/categories/', CategoryListView.as_view(), name='category-list'),
    path('blog/categories/filter/',
         CategoryFilterView.as_view(), name='category-filter'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]

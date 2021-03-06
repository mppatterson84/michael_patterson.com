from django.views.generic import ListView, DetailView
from blog.models import Post, PostCategory
from django.db.models import Q


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
            queryset = queryset
        else:
            queryset = queryset.filter(published=True)
        return queryset


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 10
    ordering = ['-pk']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
            queryset = queryset
        else:
            queryset = queryset.filter(published=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['blog_active'] = 'active'
        context['blog_aria_current'] = 'page'
        return context


class PostListAllView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = ['pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog - All Posts'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
            queryset = queryset
        else:
            queryset = queryset.filter(published=True)
        return queryset


class PostSearchView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = ['pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog Search Results'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query)
            ).distinct()
            if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
                queryset = queryset
            else:
                queryset = queryset.filter(published=True)
        else:
            queryset = None
        return queryset


class CategoryListView(ListView):
    model = PostCategory
    template_name = 'blog/category_list.html'
    ordering = ['pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog Categories'
        return context


class CategoryFilterView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = ['pk']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('category')
        if query:
            queryset = queryset.filter(
                categories__category_name=query).distinct()
            if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
                queryset = queryset
            else:
                queryset = queryset.filter(published=True)
        else:
            queryset = None
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Blog Category: {self.request.GET.get('category')}"
        return context

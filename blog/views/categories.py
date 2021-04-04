from .base import *


class CategoryListView(ListView):
    model = PostCategory
    template_name = 'blog/categories/category_list.html'
    ordering = ['pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog Categories'
        context['category_active'] = 'active'
        context['category_active_link'] = '#'
        context['category_active_sr'] = '<span class="sr-only">(current)</span>'
        return context


class CategoryFilterView(ListView):
    model = Post
    template_name = 'blog/categories/category_filter.html'
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
        context['category_filter_active'] = 'active'
        context['category_filter_active_link'] = '#'
        context['category_filter_active_sr'] = '<span class="sr-only">(current)</span>'
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = PostCategory
    template_name = 'blog/categories/category_new.html'
    login_url = '/admin/'
    success_url = reverse_lazy('category-list')
    form_class = PostCategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Blog Category'
        context['new_active'] = 'active'
        context['new_active_link'] = '#'
        context['new_active_sr'] = '<span class="sr-only">(current)</span>'
        return context


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = PostCategory
    template_name = 'blog/categories/category_delete.html'
    success_url = reverse_lazy('category-list')
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Blog Category'
        return context

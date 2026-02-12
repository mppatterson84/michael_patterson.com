from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import ProductType, Product, ProductImage
from .forms import ProductTypeForm, ProductForm, ProductImageForm, ProductImageFormSet


# ============================================================================
# Product Type Views
# ============================================================================

class ProductTypeListView(PermissionRequiredMixin, ListView):
    """List all product types."""
    model = ProductType
    template_name = 'inventory_receiving/product_type_list.html'
    permission_required = 'inventory_receiving.view_producttype'
    login_url = 'login'
    context_object_name = 'product_types'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = ProductType.objects.all().order_by('-created_at')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(code__icontains=search) |
                Q(description__icontains=search)
            )
        return queryset


class ProductTypeCreateView(PermissionRequiredMixin, CreateView):
    """Create a new product type."""
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'inventory_receiving/product_type_form.html'
    permission_required = 'inventory_receiving.add_producttype'
    login_url = 'login'
    success_url = reverse_lazy('inventory_receiving:product_type_list')


class ProductTypeUpdateView(PermissionRequiredMixin, UpdateView):
    """Update a product type."""
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'inventory_receiving/product_type_form.html'
    permission_required = 'inventory_receiving.change_producttype'
    login_url = 'login'
    success_url = reverse_lazy('inventory_receiving:product_type_list')


class ProductTypeDetailView(PermissionRequiredMixin, DetailView):
    """View details of a product type and its products."""
    model = ProductType
    template_name = 'inventory_receiving/product_type_detail.html'
    permission_required = 'inventory_receiving.view_producttype'
    login_url = 'login'
    context_object_name = 'product_type'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.filter(is_active=True).order_by('-created_at')
        return context


# ============================================================================
# Product Views
# ============================================================================

class ProductListView(PermissionRequiredMixin, ListView):
    """List all active products."""
    model = Product
    template_name = 'inventory_receiving/product_list.html'
    permission_required = 'inventory_receiving.view_product'
    login_url = 'login'
    context_object_name = 'products'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True).order_by('-created_at')
        
        # Filter by product type
        product_type = self.request.GET.get('product_type')
        if product_type:
            queryset = queryset.filter(product_type_id=product_type)
        
        # Filter by status
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        
        # Search
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(sku__icontains=search) |
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_types'] = ProductType.objects.all().order_by('title')
        context['statuses'] = Product.STATUS_CHOICES
        context['selected_product_type'] = self.request.GET.get('product_type')
        context['selected_status'] = self.request.GET.get('status')
        context['search_query'] = self.request.GET.get('search', '')
        return context


class ProductDetailView(PermissionRequiredMixin, DetailView):
    """View details of a specific product including images."""
    model = Product
    template_name = 'inventory_receiving/product_detail.html'
    permission_required = 'inventory_receiving.view_product'
    login_url = 'login'
    context_object_name = 'product'
    slug_field = 'sku'
    slug_url_kwarg = 'sku'
    
    def get_queryset(self):
        return Product.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all().order_by('sort_order', 'created_at')
        return context


class ProductCreateView(PermissionRequiredMixin, CreateView):
    """Create a new product."""
    model = Product
    form_class = ProductForm
    template_name = 'inventory_receiving/product_form.html'
    permission_required = 'inventory_receiving.add_product'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['images'] = ProductImageFormSet(self.request.POST, self.request.FILES)
        else:
            context['images'] = ProductImageFormSet()
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']
        
        if images.is_valid():
            self.object = form.save()
            images.instance = self.object
            images.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.form_invalid(form)
    
    def get_success_url(self):
        return self.object.get_absolute_url()


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    """Update an existing product."""
    model = Product
    form_class = ProductForm
    template_name = 'inventory_receiving/product_form.html'
    permission_required = 'inventory_receiving.change_product'
    login_url = 'login'
    slug_field = 'sku'
    slug_url_kwarg = 'sku'
    
    def get_queryset(self):
        return Product.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['images'] = ProductImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['images'] = ProductImageFormSet(instance=self.object)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']
        
        if images.is_valid():
            self.object = form.save()
            images.instance = self.object
            images.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.form_invalid(form)
    
    def get_success_url(self):
        return self.object.get_absolute_url()


class ProductDeleteView(PermissionRequiredMixin, UpdateView):
    """Deactivate a product (soft delete)."""
    model = Product
    fields = []
    template_name = 'inventory_receiving/product_confirm_delete.html'
    permission_required = 'inventory_receiving.delete_product'
    login_url = 'login'
    slug_field = 'sku'
    slug_url_kwarg = 'sku'
    success_url = reverse_lazy('inventory_receiving:product_list')
    
    def get_queryset(self):
        return Product.objects.filter(is_active=True)
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)


# ============================================================================
# Product Image Views
# ============================================================================

class ProductImageCreateView(PermissionRequiredMixin, CreateView):
    """Add an image to a product."""
    model = ProductImage
    form_class = ProductImageForm
    template_name = 'inventory_receiving/product_image_form.html'
    permission_required = 'inventory_receiving.add_productimage'
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        self.product = get_object_or_404(Product, sku=kwargs['sku'], is_active=True)
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.product = self.product
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.product.get_absolute_url()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.product
        return context


class ProductImageDeleteView(PermissionRequiredMixin, DeleteView):
    """Delete an image from a product."""
    model = ProductImage
    template_name = 'inventory_receiving/product_image_confirm_delete.html'
    permission_required = 'inventory_receiving.delete_productimage'
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.product = self.object.product
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return self.product.get_absolute_url()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.product
        return context


# ============================================================================
# Dashboard View
# ============================================================================

class DashboardView(PermissionRequiredMixin, ListView):
    """Dashboard showing inventory_receiving summary and recent products."""
    template_name = 'inventory_receiving/dashboard.html'
    permission_required = 'inventory_receiving.view_product'
    login_url = 'login'
    context_object_name = 'recent_products'
    
    def get_queryset(self):
        return Product.objects.filter(is_active=True).order_by('-created_at')[:10]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_products'] = Product.objects.filter(is_active=True).count()
        context['total_product_types'] = ProductType.objects.count()
        context['products_not_listed'] = Product.objects.filter(
            is_active=True,
            status=Product.STATUS_NOT_LISTED
        ).count()
        context['products_listed'] = Product.objects.filter(
            is_active=True
        ).exclude(status=Product.STATUS_NOT_LISTED).exclude(status=Product.STATUS_SOLD_OUT).count()
        context['products_sold_out'] = Product.objects.filter(
            is_active=True,
            status=Product.STATUS_SOLD_OUT
        ).count()
        return context


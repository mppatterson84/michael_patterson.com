from django.contrib import admin
from .models import ProductType, Product, ProductImage


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    """Admin interface for Product Types."""
    list_display = ['title', 'code', 'next_sku_number', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'code', 'description']
    readonly_fields = ['created_at', 'updated_at', 'next_sku_number']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'code')
        }),
        ('SKU Management', {
            'fields': ('next_sku_number',),
            'description': 'SKU numbers start at 1001 and increment automatically.'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of Product Types with products."""
        if obj and obj.products.exists():
            return False
        return super().has_delete_permission(request, obj)


class ProductImageInline(admin.TabularInline):
    """Inline admin interface for Product Images."""
    model = ProductImage
    extra = 0
    fields = ['image', 'sort_order', 'created_at']
    readonly_fields = ['created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin interface for Products."""
    list_display = ['sku', 'title', 'product_type', 'quantity_remaining', 'status', 'is_active', 'created_at']
    list_filter = ['status', 'is_active', 'is_unique', 'product_type', 'created_at']
    search_fields = ['sku', 'title', 'description']
    readonly_fields = ['sku', 'created_at', 'updated_at', 'quantity_remaining']
    inlines = [ProductImageInline]
    
    fieldsets = (
        ('Product Identity', {
            'fields': ('sku', 'product_type', 'title', 'description')
        }),
        ('Inventory', {
            'fields': ('initial_quantity', 'quantity_sold', 'quantity_remaining', 'is_unique')
        }),
        ('Physical Attributes', {
            'fields': ('length_in', 'width_in', 'height_in', 'weight_oz'),
            'classes': ('collapse',)
        }),
        ('Listing & Status', {
            'fields': ('status', 'date_listed', 'date_sold_out')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of products. Use is_active flag instead."""
        return False


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    """Admin interface for Product Images."""
    list_display = ['id', 'product', 'image', 'sort_order', 'created_at']
    list_filter = ['created_at', 'product__product_type']
    search_fields = ['product__sku', 'product__title']
    readonly_fields = ['created_at', 'image_preview']
    fieldsets = (
        ('Image', {
            'fields': ('product', 'image', 'image_preview')
        }),
        ('Organization', {
            'fields': ('sort_order',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        """Display a preview of the image."""
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-width: 200px; height: auto;" />'
        return 'No image'
    
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'

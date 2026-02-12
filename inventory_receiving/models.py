from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.urls import reverse
import math
from inventory_receiving.storages import inventory_receiving_storage


class ProductType(models.Model):
    """
    Defines a category of products and controls SKU generation.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    code = models.CharField(
        max_length=10,
        unique=True,
        help_text="Uppercase alphanumeric code used as SKU prefix (immutable)."
    )

    next_sku_number = models.PositiveIntegerField(
        default=1001,
        help_text="Next SKU number to assign for this product type."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Enforce uppercase alphanumeric codes and hyphens
        if not all(c.isalnum() or c == '-' for c in self.code):
            raise ValidationError("Product type code must be alphanumeric or contain hyphens.")
        self.code = self.code.upper()

    def __str__(self):
        return f"{self.title} ({self.code})"


class Product(models.Model):
    """
    Represents a sellable item or batch of identical items.
    """

    STATUS_NOT_LISTED = "not_listed"
    STATUS_EBAY = "ebay"
    STATUS_ETSY = "etsy"
    STATUS_WEBSITE = "website"
    STATUS_SOLD_OUT = "sold_out"

    STATUS_CHOICES = [
        (STATUS_NOT_LISTED, "Not Listed"),
        (STATUS_EBAY, "eBay"),
        (STATUS_ETSY, "Etsy"),
        (STATUS_WEBSITE, "Website"),
        (STATUS_SOLD_OUT, "Sold Out"),
    ]

    sku = models.CharField(
        max_length=50,
        unique=True,
        editable=False
    )

    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.PROTECT,
        related_name="products"
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # Inventory
    initial_quantity = models.PositiveIntegerField(
        help_text="Starting quantity (immutable after creation)."
    )
    quantity_sold = models.PositiveIntegerField(default=0)
    is_unique = models.BooleanField(default=False)

    # Physical attributes (stored as whole integers, rounded up)
    length_in = models.PositiveIntegerField(default=0)
    width_in = models.PositiveIntegerField(default=0)
    height_in = models.PositiveIntegerField(default=0)
    weight_oz = models.PositiveIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NOT_LISTED
    )

    # Lifecycle dates (mutable by design)
    date_listed = models.DateField(null=True, blank=True)
    date_sold_out = models.DateField(null=True, blank=True)

    # Soft delete
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # -------------------
    # Derived properties
    # -------------------

    @property
    def quantity_remaining(self):
        return self.initial_quantity - self.quantity_sold

    def get_absolute_url(self):
        return reverse('inventory_receiving:product_detail', kwargs={'sku': self.sku})

    # -------------------
    # Validation
    # -------------------

    def clean(self):
        # Unique product rule
        if self.is_unique and self.initial_quantity > 1:
            raise ValidationError(
                "Unique products cannot have an initial quantity greater than 1."
            )

        # Inventory consistency
        if self.quantity_sold > self.initial_quantity:
            raise ValidationError(
                "Quantity sold cannot exceed initial quantity."
            )

        # Auto sold-out enforcement
        if self.quantity_remaining == 0:
            self.status = self.STATUS_SOLD_OUT
            if not self.date_sold_out:
                self.date_sold_out = timezone.now().date()

    # -------------------
    # Save overrides
    # -------------------

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        # Round up physical dimensions and weight
        self.length_in = math.ceil(self.length_in)
        self.width_in = math.ceil(self.width_in)
        self.height_in = math.ceil(self.height_in)
        self.weight_oz = math.ceil(self.weight_oz)

        if is_new:
            # Generate SKU atomically per product type
            product_type = self.product_type
            self.sku = f"{product_type.code}-{product_type.next_sku_number}"

            product_type.next_sku_number += 1
            product_type.save(update_fields=["next_sku_number"])

        # Auto-set date_listed if transitioning from not listed
        if self.status != self.STATUS_NOT_LISTED and not self.date_listed:
            self.date_listed = timezone.now().date()

        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sku


class ProductImage(models.Model):
    """
    Stores images associated with a product.
    Images are saved under /media/products/<SKU>/.
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )

    def get_upload_to(instance, filename):
        return f"products/{instance.product.sku}/{filename}"

    image = models.ImageField(
        upload_to=get_upload_to,
        storage=inventory_receiving_storage,
    )

    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "created_at"]

    def __str__(self):
        return f"Image for {self.product.sku}"

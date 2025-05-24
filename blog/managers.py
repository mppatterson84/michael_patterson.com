from django.utils.text import slugify
from django.db import models
from django.db.models import Q


class PostManager(models.Manager):
    

    def generate_unique_slug(self, instance):
        """
        Generate a unique slug for the given instance.
        This method generates a unique slug for the Post model.
        It checks if the slug already exists in the database and appends a number
        to the slug if it does. The number is incremented until a unique slug is found.
        """
        
        # Get the base slug from the title
        base_slug = slugify(instance.title)
        # Start with the base slug
        slug = base_slug

        # Check for existing slugs that are similar
        # This will include the base slug and any slugs that match the pattern
        similar_slugs = set(
            self.filter(
                Q(slug=base_slug) |
                Q(slug__regex=rf"^{base_slug}-\d+$")
            )
            .exclude(pk=instance.pk)
            .values_list('slug', flat=True)
        )

        # print(f"Similar slugs: {similar_slugs}")

        # Increment the slug until a unique one is found
        # This loop will keep appending a number to the slug until it finds a unique one
        # The loop starts with 2 because the base slug is already counted
        i = 2
        while slug in similar_slugs:
            # print(f"Slug '{slug}' already exists. Trying with a number.")
            
            # Append a number to the base slug
            slug = f"{base_slug}-{i}"
            
            i += 1

        return slug

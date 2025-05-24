from .models import Post, PostCategory
from django import forms
from django.contrib import admin
from django.core.validators import MaxLengthValidator
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(
        label='Post Body',
        required=True,
        widget=CKEditorWidget()
    )

    image = forms.CharField(
        label='Featured Image URL',
        help_text='Required for Structured Data to provide good SEO',
        required=True,
        validators=[MaxLengthValidator(245)]
    )
    
    slug = forms.SlugField(
        label='Slug',
        help_text='Leave blank to auto-generate a slug from the title',
        required=False,
    )

    categories = forms.ModelMultipleChoiceField(
        queryset=PostCategory.objects.all(),
        required=False,
        # initial=PostCategory.objects.all()[:1]
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'image',
            'author',
            'created_at',
            'updated_at',
            'slug',
            'published',
            'categories',
        ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    # readonly_fields = ('created_at', 'updated_at')


class PostCategoryAdminForm(forms.ModelForm):
    category_name = forms.CharField()

    class Meta:
        model = PostCategory
        fields = [
            'category_name',
        ]


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    form = PostCategoryAdminForm



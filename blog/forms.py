from django import forms
from blog.models import Post, PostCategory
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Post Title",
                "class": "form-control",
                "maxlength": "50"
            }
        )
    )

    body = forms.CharField(
        label='',
        required=True,
        widget=CKEditorWidget()
    )

    published = forms.CharField(
        label='Published',
        required=False,
        widget=forms.CheckboxInput()
    )

    categories = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=PostCategory.objects.all(),
        required=False,
        # initial=PostCategory.objects.all()[:1]
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'published',
            'categories',
        ]


class PostCategoryForm(forms.ModelForm):
    category_name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Category Name",
                "class": "form-control",
                "maxlength": "50"
            }
        )
    )

    class Meta:
        model = PostCategory
        fields = [
            'category_name',
        ]

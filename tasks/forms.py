from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Task Title",
                "class": "form-control",
                "maxlength": "100"
            }
        )
    )

    detail = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Task Detail",
                "class": "form-control"
            }
        )
    )

    due_by = forms.DateTimeField(
        label="Due",
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local"
            }
        )
    )

    class Meta:
        model = Task
        fields = [
            "title",
            "detail",
            "due_by"
        ]

class TaskUpdateForm(forms.ModelForm):
    completed = forms.CheckboxInput()

    class Meta:
        model = Task
        fields = [
            "completed"
        ]
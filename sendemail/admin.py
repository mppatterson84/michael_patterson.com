from .models import Email
from django.contrib import admin

# Register your models here.

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    # fields = [('from_email', 'created_at'), 'subject', 'message',] # tuple puts fields on the same line
    fields = ['from_email', 'created_at', 'subject', 'message',]
    list_display = ('subject', 'from_email', 'created_at')
    search_fields = ('subject', 'from_email', 'created_at')
    list_filter = ('created_at',)
    readonly_fields = ('from_email', 'subject', 'message', 'created_at',)


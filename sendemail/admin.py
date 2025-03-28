from .models import Email
from django.contrib import admin

# Register your models here.

class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'from_email', 'created_at')
    search_fields = ('subject', 'from_email', 'created_at')
    list_filter = ('created_at',)

admin.site.register(Email, EmailAdmin)
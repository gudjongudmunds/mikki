# Register your models here.
from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('submitted_at', 'name', 'email', 'phone')
    readonly_fields = ('submitted_at', 'name', 'email', 'phone', 'message')

    def has_add_permission(self, request):
        return False  # Prevent adding inquiries manually

    def has_change_permission(self, request, obj=None):
        return False  # Prevent editing inquiries

    def has_delete_permission(self, request, obj=None):
        return True  # Optional: allow deletion if needed
from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'organization', 'recipient_full_name', 'recipient_department', 'visit_date', 'visit_time')
    search_fields = ('full_name', 'organization')
    list_filter = ('visit_date',)
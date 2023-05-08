from django.contrib import admin
from . models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'message', 'country_code']
    list_filter = ['created']
    date_hierarchy = 'created'
    ordering = ['created']
    

from django.contrib import admin
from Home.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date')
    list_filter = ('date',)
    search_fields = ('name', 'email')
    ordering = ('-date',)

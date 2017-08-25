from django.contrib import admin

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_display = ['full_name', 'email', 'skype']
    list_filter = ['courses']
    
    fieldsets = (
        ('Personal info', {
            'fields': ('name', 'surname', 'date_of_birth')
        }),
        ('Contact info', {
            'fields': ('email', 'phone', 'address', 'skype', 'courses')
        }),
    )

admin.site.register(Student, StudentAdmin)

from django.contrib import admin
from .models import Students


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'skype']
    search_fields = ['surname', 'email']
    list_filter = ['courses']

    fieldsets = (
        ('Персональная информация', {
            'fields': ('surname', 'name', 'date_of_birth')
        }),
        ('Контактная информация', {
            'fields': ('email', 'phone', 'address', 'skype')
        }),
        ('', {
            'fields': ('courses',)
        })
    )

    pass

admin.site.register(Students, StudentsAdmin)

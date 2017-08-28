from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ["get_name_surname", "email", "skype"]
    search_fields = ['surname', 'email']
    list_filter = ["courses"]

admin.site.register(Student, StudentAdmin)

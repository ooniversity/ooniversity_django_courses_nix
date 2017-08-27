from django.contrib import admin
from .models import Student
from courses.models import Course


class CoursesInline(admin.TabularInline):
    model = Student.courses.through
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    search_fields = ["email", "surname"]
    list_display = ["get_full_name", "email", "skype"]
    list_filter = ["courses"]
    fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
    ]
    inlines = [CoursesInline, ]


admin.site.register(Student, StudentAdmin)

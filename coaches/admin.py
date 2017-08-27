from django.contrib import admin
from .models import Coach
from courses.models import Course


class CoursesInline(admin.TabularInline):
    model = Course
    fields = ["name", "short_description"]
    extra = 0
    fk_name = 'assistant_courses'


class CoachAdmin(admin.ModelAdmin):
    # list_display = ["user.first_name", "skype", "description"]
    # list_filter = []
    # inlines = [CoursesInline, ]
    pass

admin.site.register(Coach, CoachAdmin)


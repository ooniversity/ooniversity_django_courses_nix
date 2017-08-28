from django.contrib import admin
from .models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson

class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description"]
    search_fields = [("name")]
    inlines = [LessonInline]

admin.site.site_header = 'PyBursa Administration'
admin.site.register(Course, CourseAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_display = ['description', 'subject']


admin.site.register(Lesson)

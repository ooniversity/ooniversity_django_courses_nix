from django.contrib import admin
from .models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'short_description')
    inlines = [LessonInline]

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
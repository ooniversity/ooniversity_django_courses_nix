from django.contrib import admin

from .models import Course, Lesson

class LessonInline(admin.StackedInline):
	model = Lesson

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']
    search_fields = ['name']
    inlines = [LessonInline]

class LessonAdmin(admin.ModelAdmin):
    pass



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)

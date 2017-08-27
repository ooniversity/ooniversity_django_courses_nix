from django.contrib import admin
from .models import Course, Lesson
from coaches.models import Coach


class LessonInline(admin.TabularInline):
    model = Lesson
    fields = ["subject", "description", "order"]
    extra = 0


# class CoachesInline(admin.TabularInline):
#     model = Coach
#     # fields = ["subject", "description", "order"]
#     extra = 0
#     fk_name = 'coach_courses'


class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description"]
    search_fields = ["name"]
    fields = ["name", "short_description", "description", "coach", "assistant"]
    inlines = [LessonInline]


class LessonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)


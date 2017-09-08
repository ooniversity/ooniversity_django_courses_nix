from django.contrib import admin
from .models import Coach


class CoachesAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']

    @staticmethod
    def first_name(obj):
        return obj.user.first_name

    @staticmethod
    def last_name(obj):
        return obj.user.last_name


admin.site.register(Coach, CoachesAdmin)

from django.contrib import admin

from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ["get_name", "get_last_name", "gander", "skype", "description"]

    def get_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    get_name.short_description = 'Name'
    get_last_name.short_description = 'Surname'


admin.site.register(Coach, CoachAdmin)
# Register your models here.

from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['user.first_name', 'user.last_name']
    list_filter = ['staff']

admin.site.register(Coach)

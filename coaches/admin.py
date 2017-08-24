from django.contrib import admin
from .models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'skype', 'description')


admin.site.register(Coach)
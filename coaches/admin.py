from django.contrib import admin
from .models import Coach


class CoachesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Coach)

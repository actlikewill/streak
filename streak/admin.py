from django.contrib import admin
from streak.models import Streak, Trackable

from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget


class StreakAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Trackable)
admin.site.register(Streak, StreakAdmin)
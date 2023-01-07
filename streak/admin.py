from django.contrib import admin
from streak.models import Streak, Trackable, TrackableValue

from django.contrib import admin


class TrackableInline(admin.TabularInline):
    model = TrackableValue
    extra = 1


class StreakAdmin(admin.ModelAdmin):
    inlines = [TrackableInline]


admin.site.register(Trackable)
admin.site.register(Streak, StreakAdmin)

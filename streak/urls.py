from django.contrib import admin
from django.urls import path
from streak.views import MonthView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('month/', MonthView.as_view(), name='month'),
]

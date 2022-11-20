from django.contrib import admin
from django.urls import path
from streak.views import MonthView

urlpatterns = [
    path('month/', MonthView.as_view(), name='month'),
]

from django.shortcuts import render
from django.views.generic import TemplateView
from streak.models import Streak, Trackable
import datetime
import calendar

class MonthView(TemplateView):
    template_name = 'streak/month.html'

    def get_context_data(self, **kwargs):
        # params = self.request.GET
        # print(params)
        context = super().get_context_data(**kwargs)
        now = datetime.datetime.now()
        cal = calendar.Calendar()

        weekdays = calendar.day_name
        months = calendar.month_name
        context['month'] = months[now.month]

        days = []
        for day in cal.itermonthdates(now.year, now.month):
            weekday = weekdays[day.weekday()]
            streaks = Streak.objects.filter(time__day=day.day)
            d = {
                'day': day.day,
                'weekday': weekday,
            }
            if streaks:
                d['streaks'] = streaks
            days.append(d)

        context['days'] = days


        return context
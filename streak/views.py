from django.shortcuts import render
from django.views.generic import TemplateView
from streak.models import Streak, Trackable
import datetime
import calendar

class MonthView(TemplateView):
    template_name = 'streak/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        params = self.request.GET
        params_month = params.get("month")
        params_year = params.get("year")
        if params_month:
            year = params_year or datetime.datetime.now().year
            now = datetime.datetime(int(year), int(params_month), 1)
        else:
            now = datetime.datetime.now()

        cal = calendar.Calendar()
        weekdays = calendar.day_name
        months = calendar.month_name
        context['month'] = months[now.month]

        days = []
        for day in cal.itermonthdates(now.year, now.month):
            weekday = weekdays[day.weekday()]
            streaks = Streak.objects.filter(time__date=day)
            d = {
                'day': day.day,
                'weekday': weekday,
                'month': months[day.month],
            }
            if streaks:
                d['streaks'] = streaks
            days.append(d)

        context['days'] = days

        return context

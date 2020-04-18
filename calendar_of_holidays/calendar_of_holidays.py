from datetime import date


class DayOfWeekHolidayRule:
    def __init__(self, day_of_week):
        self.day_of_week = day_of_week

    def weekday(self):
        return self.day_of_week.weekday()

    def is_holiday(self, day):
        return self.day_of_week.weekday() == day.weekday()


class DayOfMonthHolidayRule:
    def __init__(self, a_date):
        self.day = a_date.day
        self.month = a_date.month

    def is_holiday(self, a_date):
        return self.day == a_date.day and self.month == a_date.month

class DateHolidayRule:
    def __init__(self, a_date):
        self.date = a_date

    def is_holiday(self, a_date):
        return self.date == a_date

class CompoundRangeHolidayRule:
    def __init__(self, from_date, to_date, holiday_rule):
        self.from_date = from_date
        self.to_date = to_date
        self.holiday_rule = holiday_rule

    def is_holiday(self, a_date):
        return self.is_date_in_range(a_date) and self.holiday_rule.is_holiday(a_date)

    def is_date_in_range(self, a_date):
        return self.from_date <= a_date <= self.to_date


class CalendarOfHolidays:
    def __init__(self):
        self.daysOfWeekHolidayRules = []

    def set_holiday_rule(self, holiday_rule):
        self.daysOfWeekHolidayRules.append(holiday_rule)

    def is_holiday(self, a_date):
        return len(list(filter(lambda rule: rule.is_holiday(a_date), self.daysOfWeekHolidayRules))) > 0

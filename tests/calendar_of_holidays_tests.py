import unittest
from calendar_of_holidays.calendar_of_holidays import CalendarOfHolidays, DayOfWeekHolidayRule, \
    DayOfMonthHolidayRule, \
    DateHolidayRule, CompoundRangeHolidayRule
from datetime import date

"""
Indicate whether a day is holiday
- By indicating day of week, e.g: Saturday
- By indicating day and month, e.g: Dic 25th
- By indicating specific date, e.g: 08/17/2020
"""


class CalendarOfHolidaysDayOfWeekTestCases(unittest.TestCase):

    def test01_a_day_of_week_can_be_holiday(self):
        # given
        calendar = CalendarOfHolidays()
        # when
        a_saturday = date(2020, 4, 18)
        calendar.set_holiday_rule(DayOfWeekHolidayRule(a_saturday))
        another_saturday = date(2020, 4, 25)
        # then
        self.assertTrue(calendar.is_holiday(another_saturday))

    def test02_a_day_week_can_not_be_holiday(self):
        calendar = CalendarOfHolidays()
        a_monday = date(2020, 4, 20)
        self.assertFalse(calendar.is_holiday(a_monday))

    def test03_two_days_of_week_can_be_holidays(self):
        calendar = CalendarOfHolidays()
        aSunday = date(2020, 4, 19)
        calendar.set_holiday_rule(DayOfWeekHolidayRule(aSunday))

        a_saturday = date(2020, 4, 18)
        calendar.set_holiday_rule(DayOfWeekHolidayRule(a_saturday))

        self.assertTrue(calendar.is_holiday(a_saturday))
        self.assertTrue(calendar.is_holiday(aSunday))

    def test04_YYY(self):
        calendar = CalendarOfHolidays()
        a_january_first = date(2019, 1, 1)
        calendar.set_holiday_rule(DayOfMonthHolidayRule(a_january_first))
        self.assertTrue(calendar.is_holiday(a_january_first))

    def test05_YYY(self):
        calendar = CalendarOfHolidays()
        a_january_first = date(2019, 1, 1)
        calendar.set_holiday_rule(DayOfMonthHolidayRule(a_january_first))
        a_christmans = date(2019, 12, 24)
        self.assertFalse(calendar.is_holiday(a_christmans))

    def test06_YYY(self):
        calendar = CalendarOfHolidays()
        a_january_first = date(2019, 1, 1)
        calendar.set_holiday_rule(DayOfMonthHolidayRule(a_january_first))
        a_christmans = date(2019, 12, 24)
        calendar.set_holiday_rule(DayOfMonthHolidayRule(a_christmans))
        self.assertTrue(calendar.is_holiday(a_january_first))
        self.assertTrue(calendar.is_holiday(a_christmans))

    def test07_YYY(self):
        calendar = CalendarOfHolidays()
        a_date = date(2019, 1, 1)
        calendar.set_holiday_rule(DateHolidayRule(a_date))
        self.assertTrue(calendar.is_holiday(a_date))

    def test08_YYY(self):
        calendar = CalendarOfHolidays()
        from_date = date(1990, 1, 1)
        to_date = date(1999, 12, 31)
        monday_holiday_rule = DayOfWeekHolidayRule(date(2020, 4, 20))
        calendar.set_holiday_rule(CompoundRangeHolidayRule(from_date, to_date, monday_holiday_rule))
        self.assertTrue(calendar.is_holiday(date(1998, 3, 2)))

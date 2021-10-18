import calendar
from datetime import *

class MySmartCalendar:

    def __init__(self, year=2010):
        self.year = year
    
    #Function to check leap year
    def is_leap_year(self):
        if (( self.year%400 == 0)or (( self.year%4 == 0 ) and ( self.year%100 != 0))):
            return True
        else:
            return False
        
    #Function to get memorial day.Memorial day falls on last Monday of may
    def get_memorial_day(self):
        cal2 = calendar.monthcalendar(self.year, 5) #list of weeks of may.
        last_week=cal2[-1] #get last week
        last_mon=last_week[calendar.MONDAY] #get monday from last week
        return date(self.year,5,last_mon)

    #Function to get labor day. Labor day falls on first monday of September
    def get_labor_day(self):
        cal2 = calendar.monthcalendar(self.year, 9)
        first_week=cal2[0]
        second_week=cal2[1]
        if first_week[calendar.MONDAY]: #if first week has monday then get that Monday
            first_mon = first_week[calendar.MONDAY]
        else: #else get monday from second week
            first_mon = second_week[calendar.MONDAY]
        
        return date(self.year,9,first_mon)
    
    #Function to get thanksgiving day. It falls on 4th thursday of november
    def get_thanksgiving_day(self):
        cal2 = calendar.monthcalendar(self.year, 11)
        fourth_week=cal2[3]
        fifth_week=cal2[4]
        if cal2[0][calendar.THURSDAY]: #If 1st week has thursday then get that thursday from 4th week
            fourth_thur=fourth_week[calendar.THURSDAY]
        else: #else get thrusday from 5th week
            fourth_thur=fifth_week[calendar.THURSDAY]
        return date(self.year,11,fourth_thur)
    
    #Function to print calendar for the year
    def print_calendar(self):
        cal = calendar.TextCalendar(calendar.SUNDAY)
        print(cal.formatyear(self.year))
        
smart=MySmartCalendar(2020)
print(f'{smart.year} is leap year or not? {smart.is_leap_year()}')
print(f'Memorial Day: {smart.get_memorial_day()}')
print(f'Labor Day: {smart.get_labor_day()}')
print(f'Thanksgiving Day {smart.get_thanksgiving_day()}')
smart.print_calendar()
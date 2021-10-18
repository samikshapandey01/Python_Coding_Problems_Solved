import calendar
from datetime import *

#Base class to print president's day
class BaseCalendar:

    def __init__(self, year=2020):
        self.year = year
    
    #Function to print President's day: Third monday of feb
    def print_day(self):
        cal2 = calendar.monthcalendar(self.year, 2) #list of weeks of feb
        Third_week=cal2[2]
        fourth_week=cal2[3]
        if cal2[0][calendar.MONDAY]: #If 1st week has monday then get monday from 3rd week
            thir_mon=Third_week[calendar.MONDAY]
        else: #else get Monday from 4th week
            thir_mon=fourth_week[calendar.MONDAY]
        pres_day= date(self.year,2,thir_mon)
        print(f'President\'s Day of year {self.year} is "{pres_day}"')


#class to get memorial day.Memorial day falls on last Monday of may
class MemorialCal(BaseCalendar):
        
    def print_day(self):
        cal2 = calendar.monthcalendar(self.year, 5) #list of weeks of may.
        last_week=cal2[-1] #get last week
        last_mon=last_week[calendar.MONDAY] #get monday from last week
        mem_day= date(self.year,5,last_mon)
        print(f'Memorial Day of year {self.year} is "{mem_day}"')
		

#class to get labor day. Labor day falls on first monday of September
class LaborCal(BaseCalendar):
        
    def print_day(self):
        cal2 = calendar.monthcalendar(self.year, 9)
        first_week=cal2[0]
        second_week=cal2[1]
        if first_week[calendar.MONDAY]: #if first week has monday then get that Monday
            first_mon = first_week[calendar.MONDAY]
        else: #else get monday from second week
            first_mon = second_week[calendar.MONDAY]
        labor_day= date(self.year,9,first_mon)
        print(f'Labor Day of year {self.year} is "{labor_day}"')

#class to get thanksgiving day. It falls on 4th thursday of november
class ThanksgivingCal(BaseCalendar):
        
    def print_day(self):
        cal2 = calendar.monthcalendar(self.year, 11)
        fourth_week=cal2[3]
        if cal2[0][calendar.THURSDAY]: #If 1st week has thursday then get  thursday from 4th week
            fourth_thur=fourth_week[calendar.THURSDAY]
        else: #else get thrusday from 5th week
            fifth_week=cal2[4]
            fourth_thur=fifth_week[calendar.THURSDAY]
        thks_day= date(self.year,11,fourth_thur)
        print(f'Thanksgiving Day of year {self.year} is "{thks_day}"')

base = BaseCalendar(2020)
base.print_day()

mem = MemorialCal(2020)
mem.print_day()

labor = LaborCal(2019)
labor.print_day()

thanks = ThanksgivingCal(2019)
thanks.print_day()
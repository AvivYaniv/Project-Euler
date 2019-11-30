MINIMAL_YEAR = 1901
MAXIMAL_YEAR = 2000

MONTHES = 12

DESIRED_DAY_IN_WEEK = 2
PRECALCULATED_DESIRED_DAY_IN_WEEK = 6

import datetime
import calendar

# GetDayOccurencesInFirstOfMothPrecalculated(MINIMAL_YEAR, MAXIMAL_YEAR, PRECALCULATED_DESIRED_DAY_IN_WEEK)
def GetDayOccurencesInFirstOfMothPrecalculated(min_year, max_year, desired_day):
    day_in_week_conuer = 0
    year = min_year
    while year <= max_year:
        for m in xrange(1, MONTHES + 1, 1):
            day = datetime.date(year, m, 1)
            if day.weekday() == desired_day:                
                day_in_week_conuer += 1
        year += 1        
    return day_in_week_conuer

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def GetDayInWeek(self):
        d = self.day
        m = self.month
        y = self.year
        y -= m < 3
        MONTH_KEYS = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        return (y + y/4 - y/100 + y/400 + MONTH_KEYS[m-1] + d) % 7

# GetDayOccurencesInFirstOfMoth(MINIMAL_YEAR, MAXIMAL_YEAR, DESIRED_DAY_IN_WEEK)
def GetDayOccurencesInFirstOfMoth(min_year, max_year, desired_day):
    day_in_week_conuer = 0
    year = min_year
    while year <= max_year:
        for m in xrange(1, MONTHES + 1, 1):
            day = Date(1, m, year)
            if day.GetDayInWeek() == desired_day:
                day_in_week_conuer += 1
        year += 1        
    return day_in_week_conuer

# Main
def main():
    # 171
    print GetDayOccurencesInFirstOfMoth(MINIMAL_YEAR, MAXIMAL_YEAR, DESIRED_DAY_IN_WEEK)

if __name__ == "__main__":
    main()

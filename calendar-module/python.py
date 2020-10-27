import calendar

# 1. this gives you all the days of the week
#    the number dedermines how much letters 
#    you must us for each day 
#    e.g 2 = Mo Tu We Th Fr Sa Su
#    3 = Mon Tue Wed Thu Fri Sat Sun
#    in python the week starts with monday
print(calendar.weekheader(3))
print()

# 2. this gives you the number of the day starting
#    at 0 e.g Mon = 0 Tue = 1
print(calendar.firstweekday())
print()

# 3. this displays you the month and year
#    of the following parameters
print(calendar.month(2019, 3))

# 4. this displays you the month and year
#    of the following parameters in an array
print(calendar.monthcalendar(2019, 3))

# 5. this displays you the entire year 
#    of the following parameter
print(calendar.calendar(2019))

# 6. this displays you the day of the week
#    like the second example
day_of_the_week = calendar.weekday(2020, 10, 29)
print(day_of_the_week)

# 7. this tells you if the folling year you put
#    as a parameter is a leap year 
is_leap = calendar.isleap(2020)
print(is_leap)

# 7. this tells you how many leap days are
#    between the two years you put as 
#    parameters
how_many_leap_days = calendar.leapdays(2000, 3000)
print(how_many_leap_days)
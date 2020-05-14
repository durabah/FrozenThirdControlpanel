import calendar

print(calendar.weekheader(10))
print()
print(calendar.firstweekday())

print()
print(calendar.month(2020,5,2,3))

print()
print(calendar.calendar(2020))

print()
day_of_the_week = calendar.weekday(2020,5,15)
print(day_of_the_week)

is_leap = calendar.isleap(2020)
print(is_leap)

leap_days = calendar.leapdays(2000,2020)
print(leap_days)
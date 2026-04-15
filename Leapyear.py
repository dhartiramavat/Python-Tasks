import calendar

year = 2024
is_leap = calendar.isleap(year)

if is_leap:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

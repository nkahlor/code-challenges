months = [
    31, # jan
    -1, # feb
    31, # march
    30, # april
    31, # may
    30, # june
    31, # july
    31, # august
    30, # september
    31, # october
    30, # november
    31, # december
]

def is_leap_year(year):
    if year % 400:
        return True
    if year % 100:
        return False
    if year % 4 == 0:
        return True
    return False

def get_feb_days(year):
    if is_leap_year(year):
        return 29
    return 28


if __name__ == "__main__":
    sunday_on_first = 0
    # 0 = Sunday, ..., 6 = Saturday
    day_of_week = 1
    start_year = 1901
    for month in months:
        days_in_month = month if month > 0 else get_feb_days(1900)
        day_of_week = ((days_in_month % 7) + day_of_week) % 7

    for year in range(start_year, 2001):
        for month in months:
            if day_of_week == 0:
                sunday_on_first += 1
            days_in_month = month if month > 0 else get_feb_days(year)
            day_of_week = ((days_in_month % 7) + day_of_week ) % 7

    print(sunday_on_first)
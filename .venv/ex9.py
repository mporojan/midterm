def days_in_full_years(birthday, crr_day, crr_month, crr_year):
    day_str = birthday[0:2]
    month_str = birthday[3:5]
    year_str = birthday[6:]

    birth_day = int(day_str)
    birth_month = int(month_str)
    birth_year = int(year_str)

    current_day = crr_day
    current_month = crr_month
    current_year = crr_year

    def is_leap_year(y):
        if y % 400 == 0:
            return True
        elif y % 100 == 0:
            return False
        elif y % 4 == 0:
            return True
        else:
            return False

    if current_year - birth_year <= 1:
        return 0

    days_sum = 0

    for year in range(birth_year + 1, current_year):
        if is_leap_year(year):
            days_sum += 366
        else:
            days_sum += 365

    return days_sum

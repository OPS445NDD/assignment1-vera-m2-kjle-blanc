#!/usr/bin/env python3

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    # Split date string into year, month, day
    str_year, str_month, str_day = date.split('-')

    # Convert string of year, month day into integers
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    # First: divisible by 4 -> leap year
    lyear = year % 4
    if lyear == 0:
        feb_max = 29 
    else:
        feb_max = 28

    # Second: divisible by 100 -> not leap year
    lyear = year % 100
    if lyear == 0:
        feb_max = 28

    # Third: Divsible by 400 -> leap year
    lyear = year % 400
    if lyear == 0:
        feb_max = 29

    # Month length dictionary
    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    # Add one day 
    tmp_day = day + 1  # next day

    # If the number exceeds the number of days in the month of February, reset the day to 1 and increment the month
    if tmp_day > mon_max[month]:
        to_day = 1
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    # After 12 months are exceeded, move onto next year
    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month

    # Format output as year, month, day
    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def leap_year(year):
    #Divisible by 400
    if year % 400 ==0:
        return True

    # Divisible by 100, (not a leap year)
    if year % 100 ==0:
        return False

    # Divisible by 4
    if year % 4 ==0:
        return True

    # If it is not a leap year
    return False

def mon_max(month, year):
    # Determine February length based on leap year
    if leap_year(year):
        feb_days = 29
    else:
        feb_days = 28

    # Dictionary of months
    month_lengths = {
        1: 31,
        2: feb_days,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return month_lengths[month]

def valid_date(date_str):
    """Return True if date_str is a valid YYYY-MM-DD date."""
    parts = date_str.split('-')
    if len(parts) != 3:
        return False

    y, m, d = parts

    if not (y.isdigit() and m.isdigit() and d.isdigit()):
        return False

    if len(y) != 4:
        return False

    year = int(y)
    month = int(m)
    day = int(d)

    if month < 1 or month > 12:
        return False

    if day < 1 or day > mon_max(month, year):
        return False

    return True

def day_of_week(year, month, day):
    """Return the day of the week as a string: mon, tue, wed, thu, fri, sat, sun"""
    # Zeller’s congruence adjustment
    if month < 3:
        month += 12
        year -= 1

    k = year % 100
    j = year // 100

    h = (day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7

    # Zeller’s output: 0=Saturday, 1=Sunday, 2=Monday, ...
    mapping = ["sat", "sun", "mon", "tue", "wed", "thu", "fri"]

    return mapping[h]

def day_count(start, end):
    """Return number of weekend days between start and end inclusive"""
    count = 0
    current = start

    while current != after(end):
        y, m, d = current.split('-')
        dow = day_of_week(int(y), int(m), int(d))

        if dow in ("sat", "sun"):
            count += 1

        current = after(current)

    return count

def usage():
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    exit()

if __name__ == "__main__":
    import sys

    # 1. Check number of aruguments
    if len(sys.argv) !=3:
        usage()
   
    d1 = sys.argv[1]
    d2 = sys.argv[2]

  #2 Validate dates
    if not valid_date(d1) or not valid_date(d2):
        usage()

  #3 Sort Dates
    start, end = sorted([d1, d2])

  #4 Count weekends
    weekends = day_count(start, end)

  #5 Print EXACT format the checker expects
    print(f"The period between {start} and {end} includes {weekends} weekend days")

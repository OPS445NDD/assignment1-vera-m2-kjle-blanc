#!/usr/bin/env python3

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


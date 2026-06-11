#!/usr/bin/env python3

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

import datetime
import math

def sortdate(assignment):
    split_data = assignment.rsplit(' ', 2)
    if split_data[1] == 'due':
        return math.inf, math.inf, math.inf, math.inf, math.inf, math.inf
    year, month, day = split_data[1].split('-')
    hour, minute, second = split_data[2].split(':')
    return int(year), int(month), int(day), int(hour), int(minute), int(second)
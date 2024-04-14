import datetime
import math

def sortdate(assignment):
    print("sortdate....")
    split_data = assignment.split('|')[2].split(' ')
    if split_data[1] == 'Date':
        return math.inf, math.inf, math.inf, math.inf, math.inf, math.inf
    year, month, day = split_data[0].split('-')
    hour, minute, second = split_data[1].split(':')
    return int(year), int(month), int(day), int(hour), int(minute), int(second)
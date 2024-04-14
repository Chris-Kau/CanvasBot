from datetime import datetime, timedelta
from dateutil import tz

def timeconverter(date_time):
    if date_time is None:
        return "No Date"
    to_zone = tz.tzlocal()
    UTC = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%SZ')
    central = str(UTC.astimezone(to_zone))
    offset = int(central[-6:-3])
    due = date_time
    dt = datetime(int(due[:4]), int(due[5:7]), int(due[8:10]), int(due[11:13]), int(due[14:16]), int(due[17:19]))
    return dt + timedelta(hours=offset)

def time_to_word(timestr):
    if "No" not in timestr:
        dt = datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S")
        formatted_time = dt.strftime("%B %d %I:%M %p")
        return formatted_time
    return "No Date"
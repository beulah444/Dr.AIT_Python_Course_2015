#Consider a user defined class called Time that records the time of the day.
# Create a new Time object and assign attributes for hours, minutes and seconds.
# Write a function called print_time that takes a Time object and
# prints it in the form hour:minute:second.
#  Write a boolean function called is_after that takes two Time objects, t1 and t2,
#  and returns True if t1 follows t2 chronologically and False otherwise.
# Write a function called increment which adds a given number of seconds to a Time object.


import time
import datetime

class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""
    # """Time object based on datetime.datetime describes time in 24hr format"""
    def __init__(self, year=2000, month=1, day=1, hour=12, minute=0, sec=0):
        self.date = datetime.datetime(year, month, day, hour, minute, sec)

    def mktime(self):
        return time.mktime(self.date.timetuple())

ourTime = Time()
ourTime.hour = 11
ourTime.minute = 59
ourTime.second = 30


def print_time(ourTime):
    print "%.2d:%.2d:%.2d" % (ourTime.hour, ourTime.minute, ourTime.second)

print_time(ourTime)

t1 = Time(2013, 1, 3, 15)
t2 = Time(2013, 1, 3, 1)

def is_after(time1, time2):
    return time1.mktime() > time2.mktime()

print is_after(t1, t2)

incTime = Time()
incTime.hour = 11
incTime.minute = 59
incTime.second = 30


def increment(time, seconds):
    print ("Original time was: %.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

    time.second += seconds
    if time.second > 59:
        quotient, remainder = divmod(time.second, 60)
        time.minute += quotient
        time.second = remainder
    if time.minute > 59:
        quotient, remainder = divmod(time.minute, 60)
        time.hour += quotient
        time.minute = remainder
    if time.hour > 12:
        time.hour -= 12

    print "Plus %g seconds" % (seconds)
    print "New time is: %.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)

increment(incTime, 300)
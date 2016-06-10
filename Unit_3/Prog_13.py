__author__ = 'Dr.S.Gowrishankar'

class Time:
    pass

def increment(time, seconds):
    time.seconds = time.seconds + seconds

    while time.seconds >= 60:
        time.seconds = time.seconds - 60
        time.minutes = time.minutes + 1

    while time.minutes >= 60:
        time.minutes = time.minutes - 60
        time.hours = time.hours + 1

def print_time(t):
    # A function to print out a time
    print "%d:%d:%d" % (t.hours, t.minutes, t.seconds)

show_time = Time()
show_time.hours = 9
show_time.minutes = 14
show_time.seconds = 30
print 'This is the Time displayed before you increment seconds'
print_time(show_time)
print 'This is the Time displayed after you increment seconds'
increment(show_time, 5)
print_time(show_time)

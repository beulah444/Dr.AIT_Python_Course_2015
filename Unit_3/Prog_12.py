__author__ = 'Dr.S.Gowrishankar'

class Time:
    pass

def add_time(t1, t2):
    sum = Time()
    sum.hours = t1.hours + t2.hours
    sum.minutes = t1.minutes + t2.minutes
    sum.seconds = t1.seconds + t2.seconds
    return sum

def print_time(t) :
    # A function to print out a time
    print "%d:%d:%d" % (t.hours, t.minutes, t.seconds )

current_time = Time()
current_time.hours = 9
current_time.minutes = 14
current_time.seconds =  30

bread_time = Time()
bread_time.hours = 3
bread_time.minutes = 35
bread_time.seconds = 0

done_time = add_time(current_time, bread_time)

print_time(done_time)


class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """
def print_time(time):
    """
    Prints a time object in hh:mm:ss format.
    """
    print('{:02d}:{:02d}:{:02d}'.format(time.hour, time.minute, time.second))

def print_time_b(time):
    """
    Alternative way to print time.
    """
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)) 


def increment_modifier(time, seconds):
    """
    Returns the time with the added increment.
    """
    time.second += seconds
    
    time.minute = time.minute + time.second // 60
    time.second = time.second % 60
    time.hour = time.hour + time.minute // 60
    time.minute = time.minute % 60    


def increment_pure(time, seconds):

    import copy
    """
    Returns a new time object with the added increment.
    """
    time2 = copy.deepcopy(time)

    time2.second += seconds
    
    time2.minute = time2.minute + time2.second // 60
    time2.second = time2.second % 60
    time2.hour = time2.hour + time2.minute // 60
    time2.minute = time2.minute % 60

    return time2

time = Time()
time.hour = 11
time.minute = 59
time.second = 6

print("First time")
print_time(time)

increment_modifier(time, 57)

print("Time with increment")
print_time(time)

my_time = increment_pure(time, 3659)

print("time and my_time")
print_time(time)
print_time_b(my_time)

print(type(Time))
print(type(my_time))

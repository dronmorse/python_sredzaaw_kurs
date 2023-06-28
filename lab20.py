#!/usr/bin/env python3

from datetime import datetime

def TimeFunctions(parameter='m' or 'h' or 'd'):
    source_minutes = '''
def f_minutes(start, end):
    delta = end-start
    print("Difference in minutes: {}".format(divmod(delta.total_seconds(),60)[0]))
'''
    source_hours = '''
def f_hours(start,end):
    delta = end-start
    print("Difference in hours: {}".format(divmod(delta.total_seconds(),3600)[0]))
'''
    source_days = '''
def f_days(start,end):
    delta = end-start
    print("Difference in days: {}".format(divmod(delta.total_seconds(),86400)[0]))
'''
    if parameter == 'm':
        exec(source_minutes, globals())
        return f_minutes
    
    if parameter == 'h':
        exec(source_hours, globals())
        return f_hours
    
    if parameter == 'd':
        exec(source_days, globals())
        return f_days
    
delta_format = TimeFunctions(input("Please provide m, h or d: "))

start = datetime(2019, 1, 1, 0, 0, 0)  
end  = datetime.now()

print(delta_format(start,end))

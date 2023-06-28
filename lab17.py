#!/usr/bin/env python3

def calculate_paint(efficency_ltr_per_m2, *args):
    print(args)
    print("You will need {} liters of paint".format(sum(args)/efficency_ltr_per_m2))

calculate_paint(2,3,4)
calculate_paint(2,(3,4))

def log_it(*args):
    path = r"C:\Users\Open-E\Desktop\log_it.txt"
    print(args)
    process = list(args)
    print(process)
    with open(path,"w") as file:
        for i in process:
            file.write(i)
            file.write (" ")
        file.write('\n')

log_it('ERROR', 'Not enough data', 'invoices', '2020')
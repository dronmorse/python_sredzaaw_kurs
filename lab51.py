#!/usr/bon.env python3

import random

def generateTaste(number_of_values, asserted_sum):
    number_of_trials = 0
    while True:
        numbers = []
        number_of_trials += 1
        for i in range(number_of_values):
            numbers.append(random.randint(1,101))
        if sum(numbers) == asserted_sum:
            yield (number_of_trials, numbers) #as yield pauses the function the next operation will be executed on next call
            number_of_trials = 0
        
for taste in range(10):
    taste = next(generateTaste(3, 100))
    print("Number of trials: {} \n Sweet: {} Sour: {} Salty: {}".format(taste[0], 
                                                                        taste[1][0], 
                                                                        taste[1][1], 
                                                                        taste[1][2]))
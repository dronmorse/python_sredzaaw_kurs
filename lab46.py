#!/usr/bin/env python3

'''
import time

products = ["Product {}".format(i) for i in range(1, 500)]
print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 50)]
print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 500)]
print(customers)

combinations = []

for i in products:
    for j in promotions:
        for k in customers:
            combinations.append("{} - {} - {}".format(i, j, k))

for c in combinations:
    # here an analysis will be done - currently, just nothing happens :)
    pass

time.sleep(10)
'''

import time

class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0
    
    def __next__(self):
        if self.current_customer >= self.customers:
            self.current_customer = 0
            self.current_promotion += 1
        if self.current_promotion >= self.promotions:
            self.current_promotion = 0
            self.current_product += 1
        if self.current_product >= self.products:
            self.current_product = 0
            raise StopIteration()

        item_to_return = "{} {} {}".format(self.current_product, self.current_promotion, self.current_customer)
        
        self.current_customer += 1

        return item_to_return
    
    def __iter__(self):
        return self

combinations = Combinations(500, 50, 500)
print(combinations.__str__())

for i in combinations:
    print(i)


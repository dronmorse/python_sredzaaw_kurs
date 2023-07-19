#!/usr/bin/env python3

class NoDuplicates:

    def __init__(self):
        self.list = []
    
    def __call__(self,new_items):
        self.new_items = new_items
        for item in new_items:
            if item not in self.list:
                self.list.append(item)
                print("appended {}".format(item))
            else:
                pass
        return self.list

my_no_dup_list = NoDuplicates()
print(my_no_dup_list.list)
print(my_no_dup_list(['keyboard','mouse']))
print(my_no_dup_list(['keyboard','mouse','pendrive']))
print(my_no_dup_list(['pendrive','charger']))
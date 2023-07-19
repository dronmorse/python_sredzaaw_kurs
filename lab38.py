#!/usr/bin/env python3

class Cake:
    
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
    
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
    
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)
    
    def __str__(self):
        return("Kind: {}, Name: {}, Additives: {}".format(self.kind, self.name, self.additives))
    
    def __iadd__(self,other):
        additives = self.additives
        if type(other) == list:
            additives.extend(other)
        elif type(other) == str:
            additives.append(other)
        else:
            raise Exception("other types than lists and strings are not implemented yet")
        return Cake(self.name, self.kind, self.taste, additives, self.filling)
    

    
 
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
cake01 += ["radish","pomegranate"]
cake01.show_info()
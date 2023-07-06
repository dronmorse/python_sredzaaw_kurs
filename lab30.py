#!/usr/bin/env python3

class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        if name in Cake.known_types:
            pass
        else:
            Cake.known_types.append(name)
        self.name=name
        self.kind=kind
        self.taste=taste
        self.additives=additives
        self.filling=filling
        Cake.bakery_offer.append(self)
    def show_info(self):
        print('''
Name: {}
Kind: {}
Taste: {}
Additives: {}
Filling: {}
'''.format(self.name,self.kind,self.taste,self.additives,self.filling))
    
    def set_filling(self, new_filling):
        self.filling = new_filling





chocolate_cake = Cake("chocolate cake","chocolatey awesome","exquisite",r"100% bio", "CHOCOLATE")
strawberry_cake = Cake("strawberry cake","berry ok","good enough",r"99% bio", "STRAWBERRY CREAM")

chocolate_cake.set_filling("new filling")
chocolate_cake.show_info()

bakery_offer = [chocolate_cake,strawberry_cake]

for cake in bakery_offer:
    print("{} - main taste: {} \nFilled with: {} \nBio-level: {} \nTaste opinion: {}".format(cake.name,cake.kind,cake.filling,cake.additives,cake.taste))

print ("Is object an instance of Cake: {}".format(isinstance(chocolate_cake, Cake)))
print ("IObject info: {}".format(vars(chocolate_cake)))
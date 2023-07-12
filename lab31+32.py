#!/usr/bin/env python3

class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        if name in Cake.known_types:
            pass
        else:
            Cake.known_types.append(name)
        self.name=name
        self.kind=kind
        self.taste=taste
        self.additives=additives
        self.filling=filling
        self.__gluten_free = gluten_free
        if text == "" or self.kind == 'cake':
            self.__text = text
        else:
            print("text not applied as it is not a cake")
        Cake.bakery_offer.append(self)
    
    def show_info(self):
        print('''
Name: {}
Kind: {}
Taste: {}
Additives: {}
Filling: {}
Gluten free: {}
text: {}
'''.format(self.name,self.kind,self.taste,self.additives,self.filling,self.__gluten_free, self.__text))
        
    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == "cake":
            self.__text = new_text
        else:
            print("kind is not cake")
            
    Text = property(__get_text, __set_text, None, "changing the text on a cake")


cake_01 = Cake("chocolatier","cake","chocolatey","oranges","butterscotch",True, "Happy Birthday!")
cake_02 = Cake("strawberry","waffle","cream taste","oregano","whipped cream",True, "")

cake_01.show_info()
cake_01.Text = "Say what?"
cake_01.show_info()

cake_02.show_info()
cake_02.Text = "Say what?"
cake_02.show_info()

cake_01.__gluten_free = False
print(dir(cake_01))
cake_01._Cake__gluten_free = False


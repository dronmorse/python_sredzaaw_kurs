#!/usr/bin/env python3

import types

class Cake:
    
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling, gluten_free,text):
    
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))
    
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
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-'*20)
    
    def set_filling(self, filling):
        self.filling = filling
    
    def add_additives(self, additives):
        self.additives.extend(additives)
    
    def __get_text(self):
        return __text
    
    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))
    
    Text = property(__get_text, __set_text, None, 'Text on the cake')

def export_1_cake_to_html(cls, path):
    template = """
<table border=1>
        <tr>
        <th colspan=2>{}</th>
        </tr>
        <tr>
            <td>Kind</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Taste</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Additives</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Filling</td>
            <td>{}</td>
        </tr>
</table>"""
    
    with open(path, "w") as f:
        content = template.format(cls.name, cls.kind, cls.taste, cls.additives, cls.filling)
        f.write(content)

Cake.Export_1_cake_to_html = types.MethodType(export_1_cake_to_html, Cake) 

def export_all_cakes_to_html(cls, path):
    template = """
<table border=1>
        <tr>
        <th colspan=2>{}</th>
        </tr>
        <tr>
            <td>Kind</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Taste</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Additives</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Filling</td>
            <td>{}</td>
        </tr>
</table>"""
    
    with open(path, "w") as f:
        for cake in cls.bakery_offer:
            content = template.format(cake.name, cake.kind, cake.taste, cake.additives, cake.filling)
            f.write(content)

Cake.Export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)

cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, 'Good luck!')

def export_this_cake_to_html(self, path):
    template = """
<table border=1>
        <tr>
        <th colspan=2>{}</th>
        </tr>
        <tr>
            <td>Kind</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Taste</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Additives</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Filling</td>
            <td>{}</td>
        </tr>
</table>"""
    
    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)

for cake in Cake.bakery_offer:
    cake.Export_this_cake_to_html = types.MethodType(export_this_cake_to_html, cake)

#Cake.Export_1_cake_to_html(r'C:\Users\Open-E\Desktop\scripts\GIT_repositories\python_sredzaaw_kurs\1_cake.html')
Cake.Export_all_cakes_to_html(r'C:\Users\Open-E\Desktop\scripts\GIT_repositories\python_sredzaaw_kurs\all_cakes.html')

for cake in Cake.bakery_offer:
    cake.Export_this_cake_to_html(r'C:\Users\Open-E\Desktop\scripts\GIT_repositories\python_sredzaaw_kurs\{}.html'.format(cake.name.replace(' ','_')))
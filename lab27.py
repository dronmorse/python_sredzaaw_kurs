#!/usr/bin/env python3

cake_01_taste = 'vanilia'
cake_01_glaze = 'chocolade'
cake_01_text = 'Happy Brithday'
cake_01_weight = 0.7

cake_01 = {
'taste':'vanilla',
'glaze':'chocolate',
'text':'Happy Birthday',
'weight':0.7
} 

cake_02_taste = 'tee'
cake_02_glaze = 'lemon'
cake_02_text = 'Happy Python Coding'
cake_02_weight = 1.3

cake_02 = {
'taste':'tea',
'glaze':'lemon',
'text':'Happy Python Coding',
'weight':1.3
} 

cakes = [cake_01,cake_02]
     
def show_cake_info(taste, glaze, text, weight):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(taste, glaze, text, weight))

def show_single_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(cake['taste'],cake['glaze'],cake['text'],cake['weight']))

show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)

show_single_cake_info(cake_01)
show_single_cake_info(cake_02)

for cake in cakes:
    show_single_cake_info(cake)
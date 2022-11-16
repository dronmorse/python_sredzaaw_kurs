#!/usr/bin/python3

price = 123
bonus = 23
bonus_granted = True
price -= bonus if bonus_granted == True else print ("no bonus")

print (price)
rating = 5
print ("very good") if rating == 5 else print("good") if rating == 4 else print ("weak")

weekday = "Wed"
print ("pomóż mamie") if weekday == "Mon" else print ("zrób pranie") if weekday == "Tue" else print ("zrób pranie") if weekday == "Wed" else print("dyżur") if weekday == "Thu" else print("zebrania") if weekday == "Fri" else print("lekcje") if weekday == "Sat" else print("NIEDZIELA BĘDZIE DLA NAS")
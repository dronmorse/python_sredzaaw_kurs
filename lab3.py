def DisplayOptions():
    print ('1 - load data', "\n2 - export data", "\n3 - analyze & predict")
    print("Select from above or press enter to exit")
    choice = input()
    return choice

options = ['load data', 'export data', 'analyze & predict']
choice = DisplayOptions()

while choice:
    if len(choice.strip()) == 0:
        print("Please, provide something")
        choice = DisplayOptions()
    else:
        try:
            choice_num = int(choice)
        except ValueError:
            print("Please, provide an integer value")
            choice = DisplayOptions()
        else:
            if choice_num-1 < 0:
                print("Provided integer is out of range")
                choice = DisplayOptions()
            else:
                try:
                    options[choice_num-1]
                except IndexError:
                    print("Provided integer is out of range")
                    choice = DisplayOptions()
                else:
                    print("Thank you. \n%d %s\n"%(choice_num, options[choice_num-1]))
                    choice = DisplayOptions()

print ("Thank you and see you around! :)")
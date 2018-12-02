# Write the function that return the name of day with provided integer value.

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday']

def sun(integer):
    return days[0]

def mon(integer):
    return days[1]

def tue(integer):
    return days[2]

def wed(integer):
    return days[3]

def thu(integer):
    return days[4]

def fri(integer):
    return days[5]

def sat(integer):
    return days[6]

choice = True
while choice:
    integer = int(input("Enter Integer Value: "))
    if integer == 1:
        print("Today, The day is: {} ".format(sun(integer)))
        print("And integer is: {}".format(integer))

    elif integer == 2:
        print("Today, The day is: {} ".format(mon(integer)))
        print("And integer is: {}".format(integer))

    elif integer == 3:
        print("Today, The day is: {} ".format(tue(integer)))
        print("And integer is: {}".format(integer))

    elif integer == 4:
        print("Today, The day is: {} ".format(wed(integer)))
        print("And integer is: {}".format(integer))

    elif integer == 5:
        print("Today, The day is: {} ".format(thu(integer)))
        print("And integer is: {}".format(integer))

    elif integer == 6:
        print("Today, The day is: {} ".format(fri(integer)))
        print("And integer is: {}".format(integer))

    elif integer == 7:
        print("Today, The day is: {} ".format(sat(integer)))
        print("And integer is: {}".format(integer))

    else:
        print("Please enter between 1 & 7")

    choice = input("What Next? : y / n : ")
    if choice == 'n':
        integer = False
    




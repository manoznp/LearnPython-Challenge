# Write the function that return the name of day with provided integer value.

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday']

for i in range(0, len(days)):
    def day():
        return days[i]

choice = True
while choice:
    integer = int(input("Enter Integer Value: "))

    if integer == 1:
        print("Today, The day is: {} ".format(day()))
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

choice = input("What your choice Next? : y / n : ")
    if choice == 'n':
        integer = False
    




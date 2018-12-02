def StringReverse(string):
    return string[::-1]

def IsPalindrome(string):
    reverse = StringReverse(string)

    if string == reverse:
        return True
    return False


next = True
while next:
    string = input("\n\nENTER THE STRING: ")
    result = IsPalindrome(string)

    if result == True:
        print("The given string is palindrome")
    else:
        print("The given string is NOT palindrome")

    choice = input("Want to test more? y / n: ")
    if choice == 'y':
        next = True
    else:
        next = False




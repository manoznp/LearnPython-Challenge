def IsPalindrome(s):
    for i in range(len(s)//2):
        if s[i] == s[len(s)-i-1]:
            return True
        else:
            return False

next = True
while next:
    string = input("\n\nENTER THE STRING: ")
    result = IsPalindrome(string)

    if result == True:
        print("Yes, It is palindrome.")
    else:
        print("No, It is not palindrome.")

    choice = input("Want to test more? y / n: ")
    if choice == 'y':
        next = True
    else:
        next = False
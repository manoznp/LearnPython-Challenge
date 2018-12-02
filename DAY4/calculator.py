def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

firstNum = int(input("Enter First Number: "))
secondNum = int(input("Enter Second Number: "))
operator = input("What to want (+, -, *, /): ")

#Swapping Technique
if firstNum < secondNum:
    temp = firstNum
    firstNum = secondNum
    secondNum = temp

#Operations   
if operator == '+':
    print("The sum is: {} ".format(add(firstNum, secondNum)))
elif operator == '-':
    print("The substract is: {}".format(substract(firstNum, secondNum)))
elif operator == '*':
    print("The multiplication is: {}".format(multiply(firstNum, secondNum)))
else:
    print("The division is: {}".format(divide(firstNum, secondNum)))
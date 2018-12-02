lower = int(input('Enter Lower Value: ')) #4
upper = int(input('Enter Upper Value: '))#7
sum = 0
for i in range(lower, upper + 1):
    sum = sum + i

print("The total sum is{}".format(sum))

if sum%2 == 0:
    print("This number is EVEN")
else:
    print("This number is ODD")

if sum > 1:
    for i in range(2, sum):
        if sum % i == 0:
            print(sum, "is not a prime number")
            break
    else:
        print(sum, "is the prime number")
else:
    print(sum, "is not a prime number")



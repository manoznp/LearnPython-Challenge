
#TRIANGLE 
n = int(input('Enter the number of rows:'))

def triangle(n): 
    for i in range(0, n): 
        for j in range(0, i+1): 
            print("* ",end="") 
        print("\r") 

triangle(n)





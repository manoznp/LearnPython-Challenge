# write a program that syas the name has 'a' in third character or not

def Check(name):
    third_character = name[3]
    if third_character == 'a':
        print("Third character is a")
    else:
        print("Third character is not a")

names = ["haranarayan", "santosh", "shyam", "jiwan"]
# Check(names[0])
# Check(names[1])
# Check(names[2])

for i in range(0, 3):
    print(i)
    Check(names[i])

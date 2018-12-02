#Descending order

def sort_Ascending(data):
    for i in range(0, len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] < data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    print(data)

#array
a = [1,3,5,7,2,4]

#functioncall
sort_Ascending(a)
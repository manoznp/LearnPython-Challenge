
Url = input("Enter Valid Website URL: ")
Protocol = "http://"
SubUrl = Url[:7]

if SubUrl == Protocol:
    print("Valid Web Address")
else:
    print("Invalid Web Addres")

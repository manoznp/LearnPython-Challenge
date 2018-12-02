# Write the function that calculate the discount amount and discount %, and profit of an item.
def DiscountAmount():
    return MP - SP

def DiscountPercentage():
    return (DiscountAmount() / MP) * 100

def ProfitAmount():
    return SP - AP

def ProfitPercentage():
    return (ProfitAmount() / AP) * 100

def switch():
    switcher = {
        1: "The discount is {}".format(DiscountAmount()),
        2: "The discount percentage is {}%".format(DiscountPercentage()),
        3: "The Profit is {}".format(ProfitAmount()),
        4: "The Profit percentage is {}%".format(ProfitPercentage())
    }
    return switcher.get(choice, "Invalid Queries!!")


AP = int(input("Enter ActualPrice: "))
MP = int(input("Enter MarketPrice: "))
SP = int(input("Enter SellingPrice: "))


print("*************************************")

print("1. Calculate Discount Amount")
print("2. Calculate Discount Percentage")
print("3. Calculate Profit Amount")
print("4. Calculate Profit Percentage")

choice = int(input("what you like ? : "))
print(switch())
print("*************************************")


# print("The discount is {}".format(DiscountAmount()))
# print("The discount % is {}%".format(DiscountPercentage()))

# print("The Profit is {}".format(ProfitAmount()))
# print("The Profit % is {}%".format(ProfitPercentage()))
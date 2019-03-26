thePrice = input("Price of the item? ")
bef_tax = float(thePrice) * .12
new_Price = float(thePrice) - bef_tax
print("The price before tax is " + str(new_Price))
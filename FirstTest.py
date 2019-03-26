#introduction
print("Hello! Welcome to Master Store - all the Good Stuff is here!")

cust_Name = input("May I know your name, please? ")
print("Hello, " + cust_Name + "! What are you looking for?")

#selecting product
#product_list = list(["0 Bathroom set", "1 Kitchen set", "2 Home appliances", "3 Groceries"])
#product_list.sort()
#print(product_list)
#cust_Select = input("Which one would you buy? ")
#chosen_element = product_list[cust_Select]

#selecting product loop
print("Bathroom Set\nKitchen Set\nHome Appliances\nGroceries")
while True:
    cust_Select = input("Which one would you like to buy? ")

    if cust_Select == "Bathroom Set":
        print("One Bathroom Set for " + cust_Name)
    elif cust_Select == "Kitchen Set":
        print("One Kitchen Set for " + cust_Name)
    elif cust_Select == "Home Appliance":
        print("One Home Appliance for " + cust_Name)
    elif cust_Select == "Groceries":
        print("One Groceries for " + cust_Name)
    else:
        print("Can't understand that, sorry.")


    cont = input("Would like to order again?\nYes or No: ")
    while cont.lower() not in ("y","n","Y","N","Yes","No","yes","no"):
        cont = input("Would like to order again?\nYes or No: ")
    if cont == "No":
        break
    if cont == "N":
        break
    if cont == "n":
        break
#should include remembering all what the customer ordered and print it all out

print("Thank you for shopping at Master Store, " + cust_Name + ". Here are all the items that you bought " + cust_Select + ".\nThank you and Come Again!")

#yesno = input("Would you like to order again?\nYes or No")

#if yesno == "Yes":

#elif yesno == "No":
#    print("Thank you! Come again")
#else:
#    print("Can't understand that, sorry.")


#def one():
#    return "Bathroom Set"
#def two():
#    return "Kitchen Set"
#def three():
#    return "Home Appliances"
#def four():
#    return "Groceries"

#def number_switch(argument):
#    switcher = {
#        1: one,
#        2: two,
#        3: three,
#        4: four
#    }
#    func = switcher.get(argument, lambda: "Invalid choice")
#    print(func)
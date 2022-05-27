#Coffee barista 

print("Hello welcome to Flow Coffee Shop ")

#Ask customer what there name is 
name = input("What is your name?\n")

#pratice If statments 
if name == "Ben" or name == "Jeff" or name == "Loki":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input(" How many good deeds have you done today?\n"))
    if evil_status == "Yes" and good_deeds < 4:
        print("You're not welcome here" + name + "get out!!")
        exit()
    else:
        print("Hello Ben thank you for coming in today!\n\n")
else:
    print("Hello "+ name + " thank you for coming in today!\n\n" )


 
#Coffee menu 
menu = "Black Coffee, Espresso, Latte, Frappuccino, Cappucino"

#Ask what they would like 
print(name + " , what would you like from our menu today?\nHere what we have\n" + menu)


order = input()

price = 8 

if order == "Frappuccino": 
    price = 13
elif order == "Black Coffee":
    price = 3 
elif order == "Espresso":
    price = 5 
elif order == "Latte":
    price = 6 
elif order == "Cappucino":
    price = 10 
else:
    print("Sorry we don't have that here have a good day!")
    price = 0 
    exit()



quantity = input("How many coffees would you like?")

total = price * int(quantity)

#Tells total of price 
print("Thank you. Your total is: $ " + str(total))


print(  " Sounds good " + name + " I will have your " + str(quantity + order + " ready in a moment!"))
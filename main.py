print("Hello, welcome to Starkbucks Coffee!!!!!!!!!!!!!!!!!!!!!")

name = input("What is your name?\n")

menu = "Black Coffee\n" "Espresso\n" "Cappuccino\n" "Frappuccino\n"

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
      gooddeeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" and gooddeeds < 4:
        print("You are not welcome here Evil "+ name +"!! Get Out!")
        exit()

    else:
        print("Oh, you are one of those good "+ name +"s Come on in!!")

else:
    print("Hello " + name + ", thank you for coming in today.\n")

order = input(
    name +
    ", what would you like from our menu today? Heres what we are serving.\n\n" +
    menu + "\n")

quantity = input("How many coffees would you like?\n")

if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Cappuccino":
    price = 10
elif order == "Latte":
    price = 9
else:
    print("Sorry, we don't have that here")

total_price = int(quantity) * price

print("Your total will be $" + str(total_price))

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
current_price= 0.00


if size=='S':
    current_price=15
    if pepperoni == "Y":
        current_price += 2
elif size=='M':
    current_price=20
    if pepperoni == "Y":
        current_price += 3
elif size=='L':
    current_price=25
    if pepperoni == "Y":
        current_price += 3

if extra_cheese=='Y':
        current_price +=1
print(f'Your final bill is: ${current_price}.')

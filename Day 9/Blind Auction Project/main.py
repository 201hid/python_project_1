# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary



bid_data={}



def calculate_winner(users_dictionary):
    name=max(users_dictionary, key=users_dictionary.get)
    print(f'{name} has bid the highest amount {users_dictionary[name]}')


def adduserdata():
    more_user=1
    while more_user==1:\

        name=input('whats your name?')
        bid=int(input("enter your bid amount?"))
        bid_data[name]=bid
        add_More=input("Do you want to add more user? Type Yes for adding and No for not adding").lower()
        if add_More=="no":
            more_user=0
        elif add_More=="yes":
            more_user=1
            print("\n"*30)

        else:
            print("Enter Valid Input")
    else:
        print("thank you")

    calculate_winner(bid_data)

adduserdata()











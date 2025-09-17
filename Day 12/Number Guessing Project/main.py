import random
easy = 15
medium = 10
hard = 5

choice = int(input("Please enter the difficulty level (1=Easy, 2=Medium, 3=Hard): "))

if choice == 1:
    no_of_try = easy
elif choice == 2:
    no_of_try = medium
elif choice == 3:
    no_of_try = hard
else:
    print("Invalid choice! Please enter 1, 2, or 3.")


actual_number=random.randint(1,100)
while no_of_try>0:
    guess_number=int(input("Please enter your number?"))
    if guess_number==actual_number:
        print(f"Hi!!, You just guessed the number {actual_number}")
        break
    elif guess_number>actual_number:
        print(f"Hi!!, Your  guess number  {guess_number} is higher than actual number")
        no_of_try-=1

    elif guess_number<actual_number:
        print(f"Hi!!, Your  guess number  {guess_number} is lower than actual number")
        no_of_try-=1
    print(f"you have {no_of_try} guess remaining")
    if no_of_try==0:
        print(f"you just lost the game, the actual number was {actual_number} dumb!!")


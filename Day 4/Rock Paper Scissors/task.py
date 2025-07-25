import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
type_of_gestures=[rock, paper, scissors]
computer_generated_choice=random.choice(type_of_gestures)
gesture_choice_number=int(input("What is your choice sir? Type 0 for rock, 1 for Paper, 2 for scissors"))
if gesture_choice_number>=0 and gesture_choice_number<=2:
    your_gesture=type_of_gestures[gesture_choice_number]
    print(your_gesture)
    if your_gesture==computer_generated_choice:
        print('its draw try again')
    else:

        if your_gesture==rock and computer_generated_choice==scissors:
            print("You won")
        if your_gesture==rock and computer_generated_choice==paper:
            print("You lost")
        elif your_gesture == paper and (computer_generated_choice == rock or computer_generated_choice ==scissors):
            print("You lost")
        elif your_gesture == scissors and computer_generated_choice == paper :
            print("You won")
        elif your_gesture == scissors and computer_generated_choice == rock :
            print("You lost")


else:
    print("invalid response")

print("Computer Choice")
print(computer_generated_choice)

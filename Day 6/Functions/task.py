import random
no_of_lifes=6
given_word=input("hello enter your word").lower()
guessed_word=[]

for i in range(len(given_word)):
    guessed_word.append('_')
print("".join(guessed_word))







while no_of_lifes>0 and "".join(guessed_word)!= given_word:
    guess_letter=input("say me your letter you want to try").lower()
    if guess_letter in guessed_word:
        print("you have already guessed that letter")
    if guess_letter in given_word:
        for i in range(len(given_word)):
            if given_word[i]==guess_letter:
                guessed_word[i]=guess_letter

        print("".join(guessed_word))
        if "".join(guessed_word) == given_word:
            print("Your guess is correct you just won")
    else:
        print("letter not existing, you lost a life")
        no_of_lifes-=1
        print(f"You just have {no_of_lifes} remaining")
        if no_of_lifes==0:
            print("you lost")




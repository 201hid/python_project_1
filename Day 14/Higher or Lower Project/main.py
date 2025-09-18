import game_data
import random

carry_on=1
score=0
while carry_on>0:
    data_one = int(random.randint(0, 50))
    data_two = int(random.randint(0, 50))
    response=input((f"who has more followers ({game_data.data[data_one]['follower_count']}) {game_data.data[data_one]['name']} a {game_data.data[data_one]['description']}  from {game_data.data[data_one]['country']} or ({game_data.data[data_two]['follower_count']}) {game_data.data[data_two]['name']} a {game_data.data[data_two]['description']}  from {game_data.data[data_two]['country']}\nEnter A for {game_data.data[data_one]['name']} or B for {game_data.data[data_two]['name']}" )).lower()
    if response=="a":
        difference=game_data.data[data_one]['follower_count']- game_data.data[data_two]['follower_count']
    elif response=="b":
        difference=game_data.data[data_two]['follower_count']- game_data.data[data_one]['follower_count']
    else:
        print("invalid response")

    if difference>=0:
        print('you are correct')
        score+=1
    else:
        print('you are incorrect')
        carry_on=0

print(f"thanks for playing the game, you score was {score}")





# print(game_data.data[data_one]['name'], game_data.data[data_one]['country'])
# print(game_data.data[data_two]['name'], game_data.data[data_two]['country'])
# difference=game_data.data[data_one]['follower_count']-game_data.data[data_two]['follower_count']

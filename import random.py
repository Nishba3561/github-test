import random

def get_choices():
  player_choice = input("enter choice(rock,paper,scissors:")
  options = ["rock","scissors","paper"]
  computer_choice = random.choice(options)
  choices = {"player":player_choice,"computer":computer_choice}
  return choices 

def check_win(player,computer):
    print(f"you chose {player} computer chose {computer}")
    if player == computer:
     return "its a tie"
    elif player == "rock" :
     if computer== "scissors":
       return "player wins"
     else:
       return "you lose"
    elif player == "paper":
     if computer == "rock":
       return "player wins"
     else:
       return "you lose"
    elif player == "scissors": 
     if computer == "paper":
       return "player wins"
    else:
       return "you lose"
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
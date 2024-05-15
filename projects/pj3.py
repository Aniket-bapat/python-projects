import random

user_win=0
computer_win=0

while True:
    user_input =input("ROCK / PAPER / SCISSORS or Q to quit.").strip().lower()
    if user_input=="q":
        break
    
    if user_input not in ["rock", "paper", "scissors"]:
            print("Please enter valid input")
            continue
    
    computer_pick=random.choice(["rock", "paper", "scissors"])

    if user_input=="rock" and computer_pick=="scissors":
        print("You won!")
        user_win+=1
    elif user_input=="paper" and computer_pick=="rock":
         print("You won!")
         user_win+=1
    elif user_input=="scissors" and computer_pick=="paper":
         print("You won!")
         user_win+=1
    else:
         print("Computer won!")
         computer_win+=1
         continue

print("USER WINS = "+str(user_win)+"\nCOMPUTER WINS = "+str(computer_win))
print("GOOD BYEEE!!!!")        
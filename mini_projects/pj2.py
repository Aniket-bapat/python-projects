import random 
print("---------------------------------NUMBER GUESSING GAME --------------------------------")
top_of_range = input("Type a Number for uper limt \n")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0\n")
        quit()
else:
    print("Please enter a number\n")
    quit()



random_number = int((random.randrange(0,top_of_range)))

guesses=0
while True:
    guesses+=1
    user=input("GUESS A NUMBER BETWEEN 0 to " +str(top_of_range) + "\n")
    if user.isdigit():
        user=int(user)
        if user==random_number:
            print("You got it right !! \n")
            break
        else:
            print("You got it wrong!!\n")
            if user>random_number:
                print("you are above the number\n")
            else:
                print("you are below the number\n")
            continue
    else:
        print("PLEASE ENTER A NUMBER\n")
        continue

print("YOU TOOK " + str(guesses) + " GUESSES\n")
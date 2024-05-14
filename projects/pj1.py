print("WELCOME TO MY COMPUTER QUIZ\n")

playing=input("WANNA PLAY ???? \n")
playing=playing.strip().lower()

if playing!="yes":
    quit()

score=0

answer=input("What does CPU stands for?\n").lower().strip()


if answer=="central processing unit":
    print("Correct!!!")
    score+=1
else:
    print("Wrong!!!")

answer=input("What does GPU stands for?\n").lower().strip()


if answer=="graphic processing unit":
    print("Correct!!!")
    score+=1
else:
    print("Wrong!!!")

answer=input("What does html stands for?\n").lower().strip()


if answer=="hyper text markup language":
    print("Correct!!!")
    score+=1
else:
    print("Wrong!!!")

answer=input("What does CPU stands for?\n").lower().strip()


if answer=="central processing unit":
    print("Correct!!!")
    score+=1
else:
    print("Wrong!!!")

print("YOU GOT " + str(score)+ " QUSETIONS CORRECT!!")
print("Welcome to my computer quiz!")

playing = input("Do you want to Play? " )

if playing != "yes":
    quit()

print("okay! Let's play~")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("correct! ")
else: print("Incorrect ")
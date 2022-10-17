import random
import time

mylist = ["rock", "paper", "scissors", " gun"]
pscore = 0
pcscore = 0

input("Press enter to play rock, paper, scissors!")
player = input("What is your name? ")
print("Great, let's play " + player + "!")
time.sleep(0.5)
while True:
    print("Get ready!")
    time.sleep(0.5)
    print("Rock...")
    time.sleep(0.5)
    print("Paper...")
    time.sleep(0.5)
    print("Scissors...")
    time.sleep(0.5)
    print("Shoot!")
    pcchoice = random.choice(mylist)
    while True:
        pchoice = input("Enter your choice(rock, paper, scissors): ")
        if pchoice == "rock" or pchoice == "paper" or pchoice == "scissors":
            print("Looks like you picked " + pchoice + ", and I picked " + pcchoice + "!")
            time.sleep(1)
            if pchoice == pcchoice:
                print("It's a tie!")
            elif pchoice == "rock" and pcchoice == "paper" or pchoice == "paper" and pcchoice == "scissors" or pchoice == "scissors" and pcchoice == "rock":
                print("Sorry you lose!")
                pcscore += 1
            elif pchoice == "paper" and pcchoice == "rock" or pchoice == "scissors" and pcchoice == "paper" or pchoice == "rock" and pcchoice == "scissors":
                print("You win! Congradulations!")
                pscore += 1
            break
        else:
            print(pchoice + " isn't a choice silly! Try again")
            continue
    print( )
    print(player + ": " + str(pscore) + " | Computer: " + str(pcscore))
    print( )
    response = input("Would you like to play again?(y/n) ")
    if response == "y" or response == "Y":
        print("Okay " + player + ", let's do it!")
        continue
    elif response == "n" or response == "N":
        print("Thanks for playing!")
        time.sleep(1)
        break
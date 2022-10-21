import random
import time

mytupl = ("rock", "paper", "scissors")
pscore = 0
pcscore = 0

input("Press enter to play rock, paper, scissors!")
player = input("What is your name? ").capitalize()
print("Great, let's play " + player + "!")
time.sleep(0.5)
while True:
    print("Get ready!")
    time.sleep(0.4)
    print("Rock...")
    time.sleep(0.4)
    print("Paper...")
    time.sleep(0.4)
    print("Scissors...")
    time.sleep(0.4)
    print("Shoot!")
    pcchoice = random.choice(mytupl)
    while True:
        try:
            play = mytupl[int(input("Enter 1, 2, or 3 (1=rock, 2=paper, 3=scissors): ")) - 1]
            print("Looks like you picked " + play + ", and I picked " + pcchoice + "!")
            time.sleep(1)
            if play == pcchoice:
                print("It's a tie!")
            elif play == "rock" and pcchoice == "paper" or play == "paper" and pcchoice == "scissors" or play == "scissors" and pcchoice == "rock":
                print("Sorry you lose!")
                pcscore += 1
            elif play == "paper" and pcchoice == "rock" or play == "scissors" and pcchoice == "paper" or play == "rock" and pcchoice == "scissors":
                print("You win! Congradulations!")
                pscore += 1
            break
        except:
            print("Please enter 1, 2, or 3")
            continue
    print( )
    print(player + ": " + str(pscore) + " | Computer: " + str(pcscore))
    print( )
    
    response = input("Press enter to play again or x to exit: ")
    if response == "x":
        print("Thanks for playing!")
        time.sleep(1)
        break
    print("Okay " + player + ", let's do it!")
    continue

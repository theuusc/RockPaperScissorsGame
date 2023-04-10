from random import randint  #This condition will make the machine pick a random option
from time import sleep  #This condition will make an slow-mo effect after the player choose the option

itens = ("Rock", "Paper", "Scissors")
running = True

while running:
    player = None
    computer = randint(0, 2)
    
    print("-=" * 20)
    print("Welcome to the Rock Papers Scissors game")
    print('''Your options: s
    [0] Rock
    [1] Paper
    [2] Scissors''')
    print("-=" * 20)

    player = int(input("What's your choice?\n"))
    print("ROCK")
    sleep(1)
    print("PAPERS")
    sleep(1) 
    print("SCISSORS")
    print("-=" * 20)
    print("The computer chosed {}".format(itens[computer]))
    print("The player chosed {}".format(itens[player]))
    print("-=" * 20)


    if computer == 0:   #Possible macthes
        if player == 0:
            print("IT'S A TIE")
        elif player == 1:
            print("PLAYER WON")
        elif player == 2:
            print("COMPUTER WON")
        else:
            print("INVALID OPTION!!!")
    elif computer == 1:
        if player == 0:
            print("COMPUTER WON")
        elif player == 1:
            print("IT'S A TIE")
        elif player == 2:
            print("PLAYER WON")
        else:
            print("INVALID OPTION!!!")
    elif computer == 2:
        if player == 0:
            print("PLAYER WON")
        elif player == 1:
            print("COMPUTER WON")
        elif player == 2:
            print("IT'S A TIE")
        else:
            print("INVALID OPTION!!!")

    play_again = input("Play again? (y/n): ").lower()   #Condition where the player choose if wanna play again or not
    if not play_again == "y":
        running = False

print("Thanks for playing!")

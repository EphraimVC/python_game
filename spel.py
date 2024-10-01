import figures
import random

player=""
computer=""
result=""
repeat= True


class Winner:
    def __init__(self,name):
        self.name= name,

    def __str__ (self):
        return f"the winner is {self.name} "


def random_choices ():
    hands = [figures.rock, figures.paper, figures.scissors]
    selected_hand = random.choice(hands)
    return selected_hand

start = input("vill du köra Sten , Sax, Påse ? Y eller N \n")
if start.lower() == "y":
    while repeat:
        player=random_choices()
        computer=random_choices()
        print("Player 1 :")
        print(player)
        print("Computer :")
        print(computer)


        if player == figures.paper and computer == figures.rock:
            result= Winner("Player 1")
            print(result)
        elif player == figures.rock and computer == figures.scissors:
            result=Winner("Player 1")
            print(result)
        elif player == figures.scissors and computer == figures.paper:
            result=Winner("Player 1")
            print(result)
        elif player == computer:
            print("Its a Draw")
        else:
            result= Winner("Computer")
            print(result)
        again = input("continue playing ? Y or N \n")
        if again.lower() == "n":
            repeat= False
            print("Game is ended")

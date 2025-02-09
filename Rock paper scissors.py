import random

def main():
    Choices = ["paper", "rock", "scissors"]

    def Get_User_Input():
        Input_1 = input("Rock, paper, scissors: ")
        
        if Input_1.lower() in Choices:
            return Input_1
        else:
            return None
    
    User_Input = Get_User_Input()

    def Get_Comp_Input():
        Input_2 = random.choice(Choices)
        return Input_2

    Comp_Input = Get_Comp_Input()

    def Game(User_Input, Comp_Input):
        Winner = ""
        
        if User_Input.lower() == Comp_Input.lower():
            Winner = "Draw"
        elif Comp_Input != Choices[2].lower() and User_Input.lower() < Comp_Input.lower():
            Winner = "Computer"
        elif User_Input != Choices[0].lower() and User_Input.lower() < Comp_Input.lower():
            Winner = "Computer"
        elif User_Input != Choices[1].lower() and User_Input.lower() < Comp_Input.lower():
            Winner = "Computer"
        else:
            Winner = "User"

        print(User_Input)
        print(Comp_Input)
        return Winner
    
    Game_Winner = Game(User_Input, Comp_Input)

    print("The winner is " + str(Game_Winner) + " after you chose " + str(User_Input) + " ,and computer chose " + str(Comp_Input) + ".")
main()






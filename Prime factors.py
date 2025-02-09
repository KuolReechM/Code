def main():
    def Get_User_Input():
        Input = input("Enter some number: ")
        try:
            int(Input)
            Input = int(Input)
            print("This is user input: " + str(Input))
            return Input
        except ValueError:
            print("Wrong input \'" + str(Input) + "\' has been entered")
            return None

    User_Input = Get_User_Input()
    
    if User_Input is None:
        return

    def All_factors(User_Input):
        factors = []
        for counter in range(1, User_Input+1):
            if User_Input % counter == 0:
                factors.append(counter)
            else:
                pass
        
        return factors
        
    Final_Answer = All_factors(int(User_Input))

    print(str(Final_Answer))

main()
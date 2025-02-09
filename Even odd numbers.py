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
    
    def even_odd(User_input):
        Answer = ""
        if User_input % 2 == 0:
            Answer = "Even"
        else:
            Answer = "Odd"

        return Answer

    results = even_odd(int(User_Input))

    print(str(User_Input) + " is " + results)

main()
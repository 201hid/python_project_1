
def add(n1, n2):
    return round(n1 + n2,2)
def subtract(n1, n2):
    return round(n1 - n2,2)
def multiply(n1, n2):
    return round(n1 * n2,2)
def division(n1, n2):
    return round(n1 / n2,2)
current_Output=None
continue_coperation="yes"
first_number = None
second_number = None

while continue_coperation=="yes":

    operation=""
    if current_Output==None:
        first_number=int(input("Can you please enter the other  number??"))
    else:
        first_number=current_Output
    operation=input("+\n- \n* \n/ \nHi can you pick an operation")

    second_number=int(input("Can you please enter the  number??"))


    if operation=="+":
        current_Output=add(first_number, second_number)
    if operation=="-":
        current_Output=subtract(first_number, second_number)
    if operation=="*":
        current_Output=multiply(first_number, second_number)
    if operation=="/":
        current_Output=division(first_number, second_number)
    else:
        print("please enter a valid operator next time!! Try again")
        break

    print(f"your output is {current_Output}")
    if input("do you want to continue with current calculation?? type yes for continuing or no for exit")=="no":
        continue_coperation="no"






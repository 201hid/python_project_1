
def add(n1, n2):
    return round(n1 + n2,2)
def subtract(n1, n2):
    return round(n1 - n2,2)
def multiply(n1, n2):
    return round(n1 * n2,2)
def division(n1, n2):
    return round(n1 / n2,2)

continue_coperation=True
while continue_coperation==True:
    first_number=0
    second_number=0
    operation=""
    first_number==input("Can you please enter the first number??")
    operation==input("+\n- \n* \n/ \nHi can you pick an operation")

    second_number==input("Can you please enter the first number??")
    current_Output=0

    if operation=="+":
        current_Output=add(first_number, second_number)
    if operation=="-":
        current_Output=subtract(first_number, second_number)
    if operation=="*":
        current_Output=multiply(first_number, second_number)
    if division=="/":
        current_Output=division(first_number, second_number)

    print(f"your output is {current_Output}")


def format_name(f_name, l_name):
    f_name=f_name.lower()
    l_name=l_name.lower()
    for i in range(len(f_name)):
        if i==0:
            f_name_formated=f_name[i].upper()
        else:
            f_name_formated+=f_name[i]
    for i in range(len(l_name)):
        if i==0:
            l_name_formated=l_name[i].upper()
        else:
            l_name_formated+=l_name[i]

    full_name= f_name_formated + " " + l_name_formated

    return full_name




first_name=input("Please enter your first name")
last_name=input("Please enter your last name")
print(f"So your full name is {format_name(first_name,last_name)}")
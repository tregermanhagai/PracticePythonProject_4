user_string = input("Insert a string")

if user_string[0] == 'A':
    user_string = "a" + user_string[1:]
    print("change to a ", user_string )
else:
    print("The user string is: ", user_string)
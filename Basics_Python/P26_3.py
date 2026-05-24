user_email = input("Insert a an Email: \n")


if len(user_email) < 4:
    print ("Error")
else:
    if user_email[0] == '@' or user_email[-1] == '@':
        print("Error")
    else:
        print("The user email is: ", user_email)
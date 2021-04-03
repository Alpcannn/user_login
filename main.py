nick_name = "alpcan"
password = "1234"

name = input("please enter your nickname: ")
user_password = input("please enter your password: ")

if ((nick_name == name) and (password == user_password)):
    print("welcome :)")
elif ((nick_name != name) and (password == user_password)):
    print("your nick name fail bro!")
elif ((nick_name == name) and (password != user_password)):
    print("your password fail bro")
else:
    print("you can't enter ")

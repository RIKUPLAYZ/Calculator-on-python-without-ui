count = 0
login = True
name = input("Type your name: ")
o = ["tim", "john", "idk who"]
while login:

    if str(o) in name:
        user_session = True
        print("Access Granted!")
        login = False
        break
    else:
        count += 1
        attempts_left = 5 - count
        if attempts_left > 0:
            print(f"YOU HAVE {attempts_left} TRIES LEFT")
            bre
        else:
            print("Too many unsuccessful attempts.")
            login = False
            user_session = False
else:
    print("Error occurred. Please try again later.")

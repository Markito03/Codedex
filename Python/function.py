def greet(*user):
    print("Hello: ", user_name,user_age,user_sex)

user_name = input("Whats your name: ")
user_age = input("How old are you: ")
user_sex = input("What is your Gender: ")

greet(user_name, user_age,user_sex)


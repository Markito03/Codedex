guess = 0
tries = 0


while guess != 3 and tries < 3:
    guess =int(input("Guess the Number: "))
    tries = tries + 1
if tries == 3:
    print("No more tries!")
else: 
    print("Access Granted!")

pin = int(input("Type in your PIN: "))

while pin != 1234:
    pin = int(input("Wrong PIN try again: "))

if pin == 1234:
    print("Access Granted! ")
    
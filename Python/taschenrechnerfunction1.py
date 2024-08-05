zahl1 = 0
zahl2 = 0
operator = ""
def eingabe(zahl1, operator, zahl2):
    zahl1 = int(input("Erste Zahl: "))
    operator = input("+, -, *, /: ")
    zahl2 = int(input("Zweite Zahl: "))
    rechnung(zahl1, operator, zahl2)

def rechnung(zahl1, operator, zahl2):
    total = 0
    if operator == "+":
        total = zahl1 + zahl2
    elif operator == "-":
        total = zahl1 - zahl2
    elif operator == "*":
        total = zahl1 * zahl2
    elif operator == "/":
        total = zahl1 / zahl2
    print(total)
    print("Möchtest du weiter machen: ")
    antwort = input("y oder n: ")
    print(total)
    if antwort == "y":
        operator = input("+, -, *, /: ")
        zahl2 = int(input("Zweite Zahl: "))
        rechnung(total, operator, zahl2)
    else:
        exit()


eingabe(zahl1, operator, zahl2)



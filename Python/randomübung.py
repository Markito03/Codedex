import random
def add():
    return num + numt
def sub():
    return num - numt
def mul():
    return num * numt
def div():
    return num / numt
def mod():
    return num % numt
ergebnis = 0
num = random.randint(1,10)
guess = int(input("Guess a Number between 1-10: "))

while guess != num:
    guess = int(input("Wrong try again: "))
print("The right Number is: ", num)

numt = int(input("Now give me a Number: "))
print("Now you got: ", num, "and " ,numt, ".")
print( "What do you want to do with these Numbers?")
op = input("+, -, *, /, %: ") #operator
if op == "+" :
    ergebnis = add()
elif op == "-" :
    ergebnis = sub()
elif op == "*" :
    ergebnis = mul()
elif op == "/" :
    ergebnis = div()
elif op == "%" :
    ergebnis = mod()
else: 
    print("Error!")
print("Das Ergebnis ist: ", ergebnis)
print("Möchtest du weiter machen? ")
weiter = input("Y", "N" )
if weiter == "Y":
    print("Ok was möchtest du tun? ")
elif weiter == "N":
    print("Ok auf Wiedersehen! ")





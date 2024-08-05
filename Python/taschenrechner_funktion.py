def rechnung()
def plus():
    return num + numt
def minus():
    return num - numt
def mal():
    return num * numt
def div():
    return num / numt
ergebnis = 0

print("Taschenrechner") 
num = int(input("Zahl: "))
op = input("+, -, *, /: ")
numt = int(input("Zahl: "))
if op == "+":
    ergebnis = plus()
elif op == "-":
    ergebnis = minus()
elif op == "*":
    ergebnis = mal()
elif op == "/":
    ergebnis = div()
else:
    print("Error! ")
 
print("Dein Ergebnis ist: ", ergebnis)

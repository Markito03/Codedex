
print("Taschenrechner")
num = int(input("Zahl: "))
op = input("+, -, *, /: ")
numt = int(input("Zahl: "))
if op == "+":
    print(num + numt)
elif op == "-":
    print(num - numt)
elif op == "*":
    print(num * numt)
elif op == "/":
    print(num / numt)
else:
    print("Error! ")

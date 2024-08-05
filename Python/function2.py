def print_1():
    print("1")
    w = input("Willst du printen? ")
    if w == "y":
        print_1()
    else:
        exit()

print_1()
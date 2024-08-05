tasks = []

def add_tasks():
    while True:
        aufgabe = input("Was muss heute gemacht werden?  'x'  (zum beenden). ")
        if len(aufgabe) > 1:
            print(f"{aufgabe} wurde hinzugefügt. ")
            tasks.insert(0, aufgabe)
        elif aufgabe == "x":
            break
        else:
            print("Falsche eingabe versuche es nochmal")
            break
def remove_tasks():
        while True:
            print(tasks)
            entf = input("Welche Aufgabe möchtest du entfernen? 'all' (um alle zu löschen) 'x'  (zum beenden).")
            if entf == "all":
                tasks.clear()
            elif entf == "x":
                break
            elif entf.isnumeric():
                print(" Flasche eingabe probiers nochmal. ")
            elif entf.isdigit:
                tasks.remove(entf)


def uebersicht():
     print(tasks, "Das sind deine Heutigen Aufgaben. ")
     
def main():
    uebersicht()   
    add_tasks()
    uebersicht()
    answer1 = input("Möchtest du etwas entfernen? 'j' oder 'n'")
    if answer1 == 'j':
        remove_tasks()    
    elif answer1 == 'n':
        print(f"Deine Heutigen Aufgaben sind {tasks} ")
        exit()
    main()
    





main()












import random

player1 = 0
player2 = 0
name1 = ""
name2 = ""
end = 20
def würfeln(player, name):
    würfel = random.randint(1, 6)
    player += würfel
    print(name, ":", "Du hast eine ", würfel, "gewürfelt, du bist nun auf Feld nummer: ", player)
    weiter = input("")
    while würfel == 6:
        if player >= end:
            print(f"{player} hat gewonnen! ")
            break
        print("Du hast eine 6 gewürfelt, würfel nochmal...")
        weiter = input("")
        würfel = random.randint(1, 6)
        player += würfel
        print(name, ":", " Du hast eine ", würfel, "gewürfelt, du bist nun auf Feld nummer: ", player)
        weiter = input("")
    return player  

name1 = input("Spieler 1, wie möchtest du heißen: ")
name2 = input("Spieler 2, wie möchtest du heißen: ")

while True :
    input(f"{name1}: ist am Würfeln. \n")
    player1 = würfeln(player1, name1)
    if player1 >= end :
        print(name1, "hat gewonnen! ")
        break
    if player1 == player2:
        player2 = 0
        print(name2, "Wurde geschlagen und ist wieder am Start. ")
    input(f"{name2}: ist am Würfeln. \n")
    player2 = würfeln(player2, name2)
    if player2 >= end : 
        print(name2, "hat gewonnen! ")
        break
    if player2 == player1:
        player1 = 0
        print(name1, "Wurde geschlagen und ist wieder am Start. ")
    








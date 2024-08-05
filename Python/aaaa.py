import random
player1 = 0
player2 = 0
total1 = 0
total2 = 0





def würfelnp1():
    würfel = random.randint(1, 6)
    player1 =+ würfel
    total1 =+ player1
    print("P1: Du hast eine ", würfel, "gewürfelt, du bist nun auf Feld nummer: ", total)

    print("Der nächste Spieler Würfelt jetzt: ")
    weiter = input("")
    würfelnp2()

def würfelnp2():
    würfel = random.randint(1, 6)
    player2 =+ würfel
    total2 =+ player2
    print("P2: Du hast eine ", würfel, "gewürfelt, du bist nun auf Feld nummer: ", total)
    print("Der nächste Spieler Würfelt jetzt: ")
    weiter = input("")
    würfelnp1()




würfelnp1()
würfelnp2()









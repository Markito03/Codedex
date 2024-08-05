gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print("Q1) Do you like Dawn or Dusk?")

print('  1) Dawn')
print('  2) Dusk')

answer = int(input("Enter answer (1-2): "))
if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else: 
    print("Wrong input!")
print ("Q2) When I’m dead, I want people to remember me as:")

print(' 1) The Good')
print(' 2) The Great')
print(' 3) The Wise')
print(' 4) The Bold')

answer = int(input("Enter answer (1-4): "))

if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print("Wrong Input!")

print("Q3) Which kind of instrument most pleases your ear?")

print(' 1) The violin')
print(' 2) The trumpet')
print(' 3) The piano')
print(' 4) The drum')

answer = int(input("Enter answer (1-4): "))
if answer == 1: 
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer== 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print("Wrong Input!")

most_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)
if gryffindor == most_points:
  print('🦁 Gryffindor!')
elif ravenclaw == most_points:
  print('🦅 Ravenclaw!')
elif hufflepuff == most_points:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')



 
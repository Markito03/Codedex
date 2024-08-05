import random

do = 0
dt = 0
total = 0

do = random.randint(1, 6)
dt = random.randint(1, 6)

total = do + dt
tries = 0
guess = int(input("Try to guess 2-12 "))
print(total)

while guess != total:
    
    guess = int(input("Try Again! "))
    tries += 1

    if tries == 3:
        print("No more tries! ")  
        break  

if guess == total:
    print("You got it! ")
   
    
 
   


  

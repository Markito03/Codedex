height = int(input("How tall are you?"))
credits = int(input("What is your Credit Score"))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")

elif credits >= 10 or height > 137:
  print("You are not tall enough to ride.") # Erste richtig zweite falsch

elif height >= 137 or credits >= 10: 
  print("You dont have enough Credits.") #Erste richtig zweite falsch

else:
  print("You have not met either requirement")
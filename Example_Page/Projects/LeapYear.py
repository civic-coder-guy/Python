year = int(input("Which year do you want to check? "))

#Refer to the flow chart here: https://bit.ly/36BjS2D

#on every that is evenly divisible by 4
if year % 4 == 0:
  #except on every year thatis evenly divisile by 100
  if year % 100 == 0:
    #unless the year is also evenly divisible by 400
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


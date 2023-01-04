#Asks user to input there age
age = input(What is your current age?)

#Turn age into an integer
age_as_int = int(age)

#Years remaining
years = 90 - age_as_int

#Days remaining
days = years * 365

#Weeks remaining
weeks = years * 52

#Months remaining
months = years * 12

#Turn them all into a string using the f string
message = f"You have {days} days, {weeks} weeks, and {months}months left"

#print the message to the user
print(message)

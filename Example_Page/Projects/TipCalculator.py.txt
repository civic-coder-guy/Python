#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#Create a print statement for welcome message
print("Welcome to the tip calculator.")

#Ask what the total bill is, convert this into a float
bill = float(input("What was the total bill? $"))

#Ask the question of what percetange of tip you want to give, convert this to an integer
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

#Ask how many people are going to split this bill, convert to a integar 
people = int(input("How many people to split the bill? "))

#Takes the input of the user and divides it by 100 to get a float.
tip_as_percent = tip / 100

#Takes the bill and multiples the tip percent 
total_tip_amount = bill * tip_as_percent

#Takes the total tip amount and adds it to the bill amount
total_bill = bill + total_tip_amount

#Takes the total bill amount and divides it by the number of people
bill_per_person = total_bill / people

#Takes the total amount per person and and rounds it to two decimal places
final_amount ="{:.2f}".format(bill_per_person)

#Prints the final amount that each person should pay.
print(f"Each person should pay: ${final_amount}")

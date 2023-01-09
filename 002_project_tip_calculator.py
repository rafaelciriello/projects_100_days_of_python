#Tip Calculator (split the bill between friends and calculate tip)
print("Welcome to the tip calculator.")

# converting strings to float and int
bill = float(input("What was the total bill? \n$"))
tip = float(input("What the percentage tip would you like to give? 10, 12, 15? \n"))
people = int(input("How many people to split the bill? \n"))

# using mathematical operators to calculate bill and tip
total_tip = bill * (tip / 100)
total_bill = bill + total_tip
bill_per_person = total_bill / people

# formatting the result with two decimal places ":.2f"
print(f"Each person should pay ${bill_per_person:.2f}")

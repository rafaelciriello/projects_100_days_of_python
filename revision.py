print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L:\n").upper()
add_pepperoni = input("Do you want pepperoni? Y or N:\n").upper()
extra_cheese = input("Do you want extra cheese? Y or N:\n").upper()

bill = 0
print(bill)

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 20

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Yor final bill is ${bill}")

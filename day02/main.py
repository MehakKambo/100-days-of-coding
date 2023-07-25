print("Welcome to the tip calculator!")


total_amount = float(input("What is the total bill amount?\n$:"))
tip_percentage = int(input("How much tip would you like to give? \nPercent:"))
split = int(input("How many people to split the bill?\nPeople:"))

tip_amount = tip_percentage * (total_amount) / 100
total_amount += tip_amount

if split < 2:
    print(f"Each person should pay: ${total_amount}")
else:
    total_amount = total_amount / split
    print(f"Each person should pay: ${round(total_amount, 2)}")
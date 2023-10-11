#Day 2 Project: Tip Calculator.

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?\n$"))
percentage_tip = float(input("What percentage tip would you like to give?\n%"))
number_people = float(input("How many people to split the bill?\n"))


total_for_person = round((total_bill / number_people) + (total_bill * (percentage_tip / 100)) / number_people, 2)

print(f"Each person should pay: ${total_for_person}")



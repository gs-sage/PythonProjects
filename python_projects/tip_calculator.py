# Creating a simple tip calculator

print("Welcome to the Tip Calculator!")
current_bill = float(input("Enter the total bill: $"))

tip_percent = int(input("Enter the tip percent(10, 15, 20): "))

total_bill = round(current_bill + ((current_bill * tip_percent) / 100), 2)

split_bill = input("Are we splitting the bill?(Yes/No): ").lower()

if(split_bill == "yes"):
    num_people = int(input("Enter the total number of people: "))

    final_bill = round((total_bill / num_people), 2)
    print(f"You will pay a total of ${final_bill}.")

else:
    print(f"The total bill is ${total_bill}")
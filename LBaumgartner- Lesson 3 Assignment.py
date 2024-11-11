investment_amount = int(input("Enter Your Investment Amount. This is a number 1-50,000 "))
while investment_amount> 50000 or investment_amount<= 0:
    print("Your VALUE is out of RANGE! Please try again.")
    investment_amount = int(input("Please enter a new value between 0 and 50,000 "))
interest_rate = int(input("Enter Your Interest Rate. This is a number 1-15 "))
while interest_rate> 15 or interest_rate<= 0 :
    print("Your VALUE is out of RANGE. Please try again.")
    interest_rate = int(input("Please enter a new value between 1 and 15 "))
investment_duration = int(input("Enter Your Investment Duration In Years"))
while investment_duration<= 0 :
    print("Your VALUE is out of RANGE! Please try again.")
    investment_duration = int(input("Please enter a new value greater than 0"))
months = investment_duration*12 
monthly_rate= interest_rate /12 / 100
total= investment_amount
#Definitely need to go over for loops again, also F string is the best and I was wrong
for month in range(1, months + 1):
    total += investment_amount
    interest = round(total * monthly_rate, 2)
    total += interest
    if month % 12 == 0:
        print(f"year {month // 12}: ${total:}")
print(f"Investment Duration: {investment_duration} Years")
print(f"Yearly Interest Rate: {interest_rate}%")
print(f" Monthly Investment Amount: ${investment_amount}")
print(f"Total Investment Amount: ${total}")

print("Completed by Lee Baumgartner")


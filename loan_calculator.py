# Get loan details from user
money_owed = float(input("How much money do you owe in GBP?\n"))
annual_percent_rate = float(input("What is the annual percentage rate of the loan?\n"))
payment = float(input("How much will you pay every month?\n"))
months = int(input("How many months you want to see the result for?\n"))

monthly_rate = (annual_percent_rate/100)    # calculate in percent
monthly_rate = monthly_rate / 12            # calculate per month

for i in range(months):
    # interest to pay
    interest_paid = money_owed * monthly_rate

    # adding the interest
    money_owed = money_owed + interest_paid

    # check if loan has been paid off
    if (money_owed - payment) < 0:
        print('The last payment is ', money_owed)
        print('You paid off the loan in ', i + 1, ' months')
        break

    # deduct the payment made for the month
    money_owed = money_owed - payment


    print("Paid", payment, "of which", interest_paid, "was interest.", end=" ")
    print("Now I owe", money_owed)


# Test values
# money_owed = 50000
# annual_percent_rate = 3
# payment = 1000
# months = 100, NOTE: The loan gets paid OFF in 54 months
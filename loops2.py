totalExpenseItems = int(input('Enter the total number of items you want to input:'))
print('So you want to enter ' + str(totalExpenseItems) + ' items?? Here you go...')

expenses = []
expense_categories = []
grouped_total = []
for i in range(totalExpenseItems):
    expense_category = input("Enter expenese category (food/ travel/ stay):")
    expense_cost = float(input("How much did you spend for '" + expense_category + "': "))
    expense_item = [expense_category, expense_cost]
    expenses.append(expense_item)
    if expense_category not in expense_categories:
        expense_categories.append(expense_category)
        grouped_total.append(0)
    category_index = expense_categories.index(expense_category)
    grouped_total[category_index] += expense_cost

for item in expenses:
    print(item)

print("You had expenses in the categories: ", expense_categories)
print("Amount you spent for each category: ", grouped_total)
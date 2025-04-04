expense_data = [
    [11.5, 'Main meal'],
    [3, 'Travel'],
    [1.89, 'Drink'],
    [55, 'Stay'],
    [2.33, 'Snack'],
    [11.5, 'Food'],
    [1.32, 'Snack'],
    [0.55, 'Snack'],
    [7.89, 'Travel'],
    [5.43, 'Drink']
]

food_total = 0.0
stay_total = 0.0
travel_total = 0.0

for item in expense_data:
    if item[1] == 'Food' or \
            item[1] == 'Snack' or \
            item[1] == 'Main meal' or \
            item[1] == 'Drink':
        food_total += item[0]
    elif item[1] == 'Travel':
        travel_total += item[0]
    elif item[1] == 'Stay':
        stay_total += item[0]

print('Food total: £', food_total, sep='')
print('Stay total: £', stay_total, sep='')
print('Travel total: £', travel_total, sep='')

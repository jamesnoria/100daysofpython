# For user
print('==Welcome to the tip calculator==')
bill = float(input('What whas the total bill?: $'))
percentage = int(input('What percentage tip would you like to give? 10, 12 or 15: '))
people = int(input('How many people to split the bill?: '))
# Logic
percentage_operator = percentage / 100
total_tip = bill * percentage_operator
people_cut = round((total_tip / people), 2)
# Result
result = f'Each one should pay: ${people_cut}'
print(result)
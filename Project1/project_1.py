operation = input('''
Please select an operator to use:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Enter first number: '))
number_2 = int(input('Enter second number: '))

# Addition
if operation == '+':
	print ('{} + {} ='.format(number_1, number_2))
	print (number_1 + number_2)

# Subtraction
elif operation == '-':
	print ('{} - {} ='.format(number_1, number_2))
	print (number_1 - number_2)

# Multiplication
elif operation == '*':
	print ('{} * {} ='.format(number_1, number_2))
	print (number_1 * number_2)

# Division
elif operation == '/':
	print ('{} / {} ='.format(number_1, number_2))
	print (number_1 / number_2)

else:
	print('Invalid operator selected.  Exiting program.')

# Followed guide at https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3 provided in Canvas to write script.
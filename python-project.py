import os
print("Hello world!")
print("This is a python application")
print("Welcome to my calculator")
print("press enter to continue....")
input()
os.system('clear')
x = int(input('Enter the number1 \n'))
os.system('clear')
y = int(input('Enter the number2 \n'))
os.system('clear')
z = int(input('Enter the number for the calculation \n if you want to + enter number 1 \n if you want to - enter number 2 \n if you want to / enter number 3 \n'))
if z == 1:
    print(f'The sum of {x} and {y} is {x+y}')
elif z == 2:
    print(f'The difference of {x} and {y} is {x-y}')
elif z == 3:
    print(f'The quotient of {x} and {y} is {x/y}')
else:
    print('Invalid input. Please enter 1, 2, or 3.')
            

def two_num(): #A function that takes only numerical values from the user.
 while True:
    try:
        num_1 = float(input('Enter first number: '))
        break
    except ValueError:
        print('Enter a valid number')

 while True:
    try:
        num_2 = float(input('Enter second number: '))
        break
    except ValueError:
        print('Enter a valid number')
 return num_1,num_2
 

def choice_2():#Unpack the values from the user.
 num_1, num_2 = two_num()
 return num_1,num_2

num_1, num_2 = choice_2()



def addition(num_1,num_2):
    return f'{num_1} + {num_2} = {num_1 + num_2}'

def subtraction(num_1,num_2):
    return f'{num_1} - {num_2} = {num_1 - num_2}'

def multiplication(num_1,num_2):
    return f'{num_1} * {num_2} = {num_1 * num_2}'

def division(num_1,num_2):
    if num_2 == 0:
        return 'Error: Division by zero is not allowed.'
    else:
     return f'{num_1} / {num_2} = {num_1/num_2}'

def menu():
 print("""
1.Input (1) for Addition
2.Input (2) for Subtraction
3.Input (3) for Multiplication
4.Input (4) for Division
5.Input (5) for new values
5.Input (6) to Exit               
""")
 option = input('Choice: ')
 return option


option = menu()
#The User is giving options to choose from until exiting the program
while option.lower != '5':
    if option == '1':
        print(addition(num_1,num_2))
        option = menu()
    elif option == '2':
        print(subtraction(num_1,num_2))
        option = menu()
    elif option == '3':
        print(multiplication(num_1,num_2))
        option = menu()
    elif option == '4':
        print(division(num_1,num_2))
        option = menu()
    elif option == '5': 
       num_1,num_2 = choice_2() # Ensure new values are unpacked 
       option = menu()
       
    elif option == '6':
        break
    else:
        print('Invalid input')



    




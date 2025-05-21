# This is a simple calculator program that performs basic arithmetic operations
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operation = {'+': add, '-': sub, '*': multiply, '/': divide}

def calculator():
        first_number = float(input('Enter first number: '))
        should_repeat = True
        while should_repeat:
            operator = input('Enter operation: ')
            second_number = float(input('Enter second number: '))
            result = operation[operator](first_number, second_number)
            print(f"{first_number}{operator}{second_number} = {result}")
            do_continue = input('Do you want to continue with same number? y or n')
            if do_continue == 'y':
                first_number = result
            else:
                should_repeat = False
                print('\n' * 40)
                calculator()

calculator()


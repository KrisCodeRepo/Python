# Subscripting
print('Hello'[-1])

print('123'+'345') #String

#Integer = Whole number
print(123+345)

#Large Integers
print(123_456_789)

#float
print(3.13)

#Boolean
print(True)
print(False)


# Type Conversion
# You can convert data into different data types using special functions. e.g.

# float()

# int()

# str()

print(type(123))
print(type('123'))
print(type(True))
print(type(123.67))
#Type conversion
print(int('123') + int('456'))

print("My age: " + str(12))
print(123+456)
print(456-87)
print(12*12)
print(7/2)
print(7//2)
print(2**3)

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

bmi = 85/ 1.72**2
print(bmi)
print(type(bmi))

# Assignment Operator

Score = 0

Score += 1
print(Score)

height = 1.8
is_winning = True
print(f"Your score is {Score}, your height is {height}, your winning is {is_winning}")

print(6 + 4 / 2 - (1 * 2))
#PEMDAS  
(6 + 4 / 2 - 2) # Parentheses, Exponents, Multiplication and Division, Addition and Subtraction
(6 + 2 - 2)
# 1. Parentheses: Perform calculations inside parentheses first.
# 2. Exponents: Calculate powers and roots next

## Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percentage = tip / 100
final_bill = bill + (bill * tip_percentage)
to_be_paid = final_bill / people
print(f"Your tip amount is {to_be_paid:.2f}")






#If/else Statements
# If the height is greater than 120 cm, they can ride the rollercoaster
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print('You can ride the rollercoaster!')
else:
    print('You can not ride the rollercoaster!')

#if elif, else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    if age >= 18:
        print("Please pay $12.")
    elif age < 12:
        print("Please pay $5.")
    else:
        print("Please pay $7.")
else:
    print("Sorry you have to grow taller before you can ride.")

# Modulo
print("Welcome to number check")
num = int(input('Enter the number : '))
if num % 2 == 0:
    print(num, 'is an even number.')
else:
    print(num, 'is an odd number.')

# Python Pizza
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == 'S':
    bill = 15
    if pepperoni == 'Y':
        bill +=2
elif size == 'M':
    bill = 20
    if pepperoni == 'Y':
        bill +=3
elif size == 'L':
    bill = 25
    if pepperoni == 'Y':
        bill +=3
if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")

# Logical Operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >=45 and age <=55:
        #45 <= age <= 55
        print("You can have the free ride!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    #
    # wants_photo = input("Do you want a photo taken? Y or N. ")
    # if wants_photo == "Y":
    #     bill += 3
    #
    # print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

#Treasure Island Game
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right =input('You\'re at cross road. Where do you want to go?\nType "left" or "right" ').lower()
if left_right == 'left':
    print('You have come to a lake. There is an island in the middle of the lake.')
    wait_swim =input('Type "wait" to wait for the boat. Type "swim" to swim across').lower()
    if wait_swim == 'wait':
        door = input('Select a Door\nRed Yellow Blue')
        if door =='red':
            print('Burned by fire\nGame over')
        elif door =='Yellow':
            print('You win!')
        elif door =='Blue':
            print('Eaten by beasts')
        else:
            print('Game over')
    else:
        print('Attacked by trout.\nGame Over.')

else:
    print('Fall in hole.\n Game Over.')

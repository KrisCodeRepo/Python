import random

# import my_module
#generate random int using randint()
randint = random.randint(30,140)
print(randint)
# print(my_module.my_fav_number)
random_num_0_to_1 = random.random()
random_num_0_to_10 = random.random() * 10
random_flt = random.uniform(5, 10)
#
print(random_num_0_to_1)
print(random_num_0_to_10)
print(random_flt)

#Random Heads or Tails

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print('Heads')
else:
    print('Tails')

#Lists
states_of_india=['Andhra Pradesh','Arunachal Pradesh','Jammu & Kashmir'
                 'Karnataka','Kerala','Madhya Pradesh','Maharashtra',
                 'Tamilnadu']
print(states_of_india[-2])
#Can update list like below
states_of_india[2] = 'J&K'
print(states_of_india[2])
#Can add new items to end of list like below
states_of_india.append('GOA')
print(states_of_india[-1])
#Extending list with another list
#Can add multiple items to end of list like below
states_of_india.extend(['Himachal Pradesh','Uttarakhand'])
print(states_of_india[-2])
print(states_of_india)

#Random from list
import  random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#1
print(random.choice(friends))

#2
randint = random.randint(0,4)
print(friends[randint])

#Get number of items in list
#len() function returns number of items in list
print(len(friends))

#RockPaperScissors-Using random module
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = input('What do you choose??\nType 0 for rock, 1 for paper, 2 for scissors\n')
if user_choice >= '0' and user_choice <= '2':
    print(game_images[int(user_choice)])

computer_choice = random.randint(0,2)
print(game_images[computer_choice])

if int(user_choice) >=3 or int(user_choice) < 0:
    print('You typed invalid input. You lose!')
elif user_choice == 0 and computer_choice == 2:
    print('You win!')
elif computer_choice == 0 and user_choice == 2:
    print('You lose!')
elif computer_choice > int(user_choice):
    print('You lose!')
elif int(user_choice) > computer_choice:
    print('You win!')
elif computer_choice == int(user_choice):
    print('Draw')
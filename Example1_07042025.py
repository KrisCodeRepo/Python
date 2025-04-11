#This prgram says hello and asks for your name.

#Data Types - str, int, float
#To convert int to str use str(var) and vice versa
#str * 3 give same string thrice

print('Hello World!') #print function used to print
print('What is your name?') #ask for there name
myName = input() #input() function used to ask for user input
print('It is good to meet you, ' +myName)
print('The length of your name is:')
print(len(myName)) #len() function used to calculate length of string
print('What is your age?') #ask for their age
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in a year.')
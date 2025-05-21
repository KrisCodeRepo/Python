fruits =['apple', 'banana', 'cherry']
for fruit in fruits:
    #Indentation is important in Python. Here the print statement is indented to be part of the for loop.
    print(fruit)
    print(fruit + " pie")
#Here the print is not indented, so it is not part of the for loop.
print(fruits)

#max logic
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
max_num = 0
for score in student_scores:
    if score > max_num:
        max_num = score
print('max_num' + str(max_num))

#Range function within loop - sum of 1 to 100
sum = 0
for number in range(1,101):
    sum += number
print(sum)
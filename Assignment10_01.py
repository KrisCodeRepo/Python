#read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re
name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_42.txt"
handle = open(name)
numbers = list()
for line in handle:
    # Find all numbers in the line using regex
    nums = re.findall('[0-9]+', line)
    # Convert found strings to integers and extend the numbers list
    numbers.extend([int(num) for num in nums])
# Compute the sum of the numbers
total = sum(numbers)
# Print the total sum
print("Total sum of numbers:", total)
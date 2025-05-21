largest = None
smallest = None
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        num= int(user_input)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except:
        print("Invalid input")
if largest is not None and smallest is not None:
    print("Maximum is", largest)
    print('Minimun is', smallest)
else:
    print("No valid numbers were entered.")

score = input("Enter Score: ")
try:
    s = float(score)
except:
    print("Error: Invalid input")
    exit()
# Check if the score is within the valid range
if s>0.0 and s<=1.0:
    if s>=0.9:
        print("A")
    elif s>=0.8:
        print("B")
    elif s>=0.7:
        print("C")
    elif s>=0.6:
        print("D")
    else:
        print("F")
else:
    print("Error: Score is out of range")
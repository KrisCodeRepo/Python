l1 = [2,4,3]
l2 = [5,6,4]    

def addTwoNumbers(l1, l2):
    l3 = []
    l3 = l1 + l2
    carry = 0   
    for i in range(len(l3)):
        if i < len(l1) and i < len(l2):
            sum_value = l1[i] + l2[i] + carry
        elif i < len(l1):
            sum_value = l1[i] + carry
        else:
            sum_value = l2[i] + carry
        
        carry = sum_value // 10
        l3[i] = sum_value % 10
    if carry > 0:
        l3.append(carry)
    return l3
# Example usage:
result = addTwoNumbers(l1, l2)
print(result)  # Output: [7, 0, 8]
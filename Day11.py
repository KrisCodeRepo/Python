def is_prime(num):
    is_true = True
    if num < 2:
        return False
    elif num % 2 == 0 and num != 2:
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
    return True

is_TRF = is_prime(3)
print(is_TRF)

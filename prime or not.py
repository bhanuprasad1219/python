def is_prime_basic(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
num = 987
b= is_prime_basic(num)
print(b)

# nth prime numbers






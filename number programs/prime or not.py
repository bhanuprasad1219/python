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


def prime_(num):
    if num > 1:
        for num in range(2,num+1):
            for i in range(2,num):
                if num%i == 0:
                    break
            else:
                print(num)
print(prime_(100))






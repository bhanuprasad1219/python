def perfect_number(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum == n


count = 0
for x in range(6, 1000):
    if perfect_number(x):
        count += 1
print(count)




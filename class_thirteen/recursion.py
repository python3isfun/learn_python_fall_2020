

sum = 0
for i in range(0, 11):
    sum += i
print (sum)


def sum_to(n):
    sum = 0
    for i in range(0, n+1):
        sum += i
    return sum

print (sum_to(10))

def sum_me(n):
    if n == 1:
        return 1
    return n + sum_me(n-1)

print (sum_me(10))
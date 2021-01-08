
def fib(n, m, x):
    if m > x:
        return
    print (m)
    fib(m, n + m, x)

def fib(t):
    n = 0
    m = 1
    print (n)
    for i in range(0, t+1):
        print (m)
        k = n
        n = m
        m = k + m

# print (fib(0, 1, 1000000))
print (fib(100))
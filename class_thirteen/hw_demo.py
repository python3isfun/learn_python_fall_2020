# 0 1
# starting of our sequence
#
# n = 0
#
# m = 1
#
# x = m + n
# # x will be 1
#
# x_one = x + m
# # x_one will be 2
#
# x_two = x_one + x
# # x_two will be 3
#
# x_three = x_two + x_one
# # x_three will be 5
#
# x_four = x_three + x_two
#
# a = 0
# b = 1
# for i in range(1, 10):
#     x = a
#     # first loop: x is a new variable in our loop to keep the n-2 indexed value
#     # second loop, a = 1, x = 1, b = 1
#     # third loop: a = 1, x = 1, b = 2
#     # four loop: a = 2, b = 3, x = 2
#     # fifth loop: a = 3, b = 5, x = 3
#     # sixth loop: a = 5, b = 8, x = 5
#     # seventh loop: a = 8, b = 13, x = 8
#     # eighth loop: a = 13, b = 21, x = 13
#     a = b
#     # first loop, x = 0, a = 1, b is  also 1
#     # second loop, x = 1, a = 1, b = 1
#     # third loop, x = 1, b = 2, a = 2
#     # fourth loop: x = 2, b = 3, a = 3
#     # fifth loop: x = 3, b = 5, a = 5
#     # sixth loop: x = 5, b = 8, a = 8
#     # seventh loop: x = 8, b = 13, a = 13
#     # eighth loop: x = 13, b = 21, a = 21
#     b = a + x
#     # first loop: b will still be 1, a is 1, b = 1,
#     # second loop: x = 1, a = 1, b = 2
#     # third loop: a = 2, x = 1, b = 3
#     # fourth loop: a = 3, x = 2, b = 5
#     # fifth loop: a = 5, x = 3, b = 8
#     # sixth loop: a = 8, x = 5, b = 13
#     # seventh loop: a = 13, x = 8, b = 21
#     # eighth loop: a = 21, x = 13, b = 34
#     print (b)
#     if b > NUM:
#         break

#
# def function_one(name):
#     print ("hello " + name)
#     name = name + name
#     if len(name) > 10:
#         return
#     function_one(name)
#
# function_one("Aidan")

def print_fib(n, m):
    # first call, n = 0, m = 1
    # second call, n = 1, m = 1
    # third call, n = 1, m = 2
    # fourth call, n = 2, m = 3
    # fifth call, n = 3, m = 5
    # sixth call, n = 5, m = 8
    # seventh call, n = 8, m = 13
    # eighth call, n = 13, m = 21

    if m > 100:
        return
    print (m)
    print_fib(m, n+m)
    # first call print_fib(1, 1)
    # second call, print_fib(1, 2)
    # third call, print_fib(2, 3)
    # fourth call, print_fib(3, 5)
    # fifth call, print_fib(5, 8)
    # sixth call, print_fib(8, 13)
    # seventh call, print_fib(13, 21)
    # eighth call, print_fib(21, 34)



a = 0
b = 1
# print (0)
# print_fib(0, 1)


def print_fib(n, m):
    if m > 10:
        return
    print (m)
    print_fib(m, n+m)



def print_fib(a, b, n):
    for i in range(1, 100):
        x = a
        a = b
        b = x + a
        if b > 100:
            break
        print (b)

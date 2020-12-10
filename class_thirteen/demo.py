

# sum = 0
# for i in range(0, 101):
#     sum += i
#
# print (sum)
#
# def calculate_sum(n):
#     # if input is 10, this will return 55
#     # if input is 100, this will return 5050
#     sum = 0
#     for i in range(0, n+1):
#         sum += i
#     return sum
#
#
# def get_sum_dictionary(n):
#     d = {}
#     for i in range(0, n+1):
#         d[i] = calculate_sum(i)
#     return d
#
# print (get_sum_dictionary(1000))
# # print (calculate_sum(10))
#
# def function_one(n):
#     # at this line, n is 10
#     print ("current n")
#     print (n)
#     if n < 0:
#         print ("end of recursion here")
#         return 0
#     else:
#         return function_one(n - 1)
#
# print (function_one(10))

def calculate_sum(n):
    sum = 0
    for i in range(0, n+1):
        sum += i
    return sum


def calculate_sum(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum(n-1)

print (calculate_sum(10))
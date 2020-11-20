

# def print_value(value):
#     print("Hello, " + value)
#     s = input()
#     print ("Your name is " + s)
#     return s
#
# x = 4
# x = print_value("please tell me your name")
# print ("I got this from my function " + x)
#
#
# def convert_to_celcius(farenheit):
# #     return 10
#
# s = "apple is good"
# d = {"apple":"orange"}
# for k, v in d.items():
#     print (k, v)
#     print (s.replace(k, v))
#     print (s)
'''
5 8 6 9
2 1 9 7
'''

list = ['5', '8', '6', '9', '2', '1', '9', '7']

h = 0
newlist = []
for i in range(int(len(list) / 4)):
    newlist.append(abs(int(list[h]) - int(list[h + 2])))
    h = h + 1
h = 4
for i in range(int(len(list) / 4)):
    newlist.append(abs(int(list[h]) - int(list[h + 2])))
    h = h + 1
print(newlist)
h = 0
sum = 0
for i in range((int(len(newlist) / 2))):
    sum = sum + (int(newlist[h]) * int(newlist[h + 1]))
    h = h + 2
print(sum * sum, "is the square area.")


def calculate_sum(n):
    r = 0
    # you will add logic here to compute a return value r
    return r
#
# def five_times(n):
#     return 5 * n

print (calculate_sum(20))

# print (calculate_sum(5))

# You are given a input file called temperatures.txt.
# In this file there are multiple lines.
# each line has some numbers.
# Your task is read this file, and provide three outputs of all the numbers.
# The smallest number in the file, the largest number in the file, and the average of all numbers in the file.

# example file

# 1 2 3
# 1
# 4

# In the above example, there are three lines, totally five numbers in the file.
# the output after processing the input file should be printed as:
# the smallest number is 1.
# the largest number is 4
# the average of all numbers is 2.2

big_list = []
smallest_number = None

with open("temperatures.txt", "r") as fin:
    for line in fin:
        fs = line.split()
        for f in fs:
            big_list.append(int(f))

print  (big_list)

for n in big_list:
    if smallest_number == None:
        smallest_number = n
    else:
        if smallest_number > n:
            smallest_number = n

print (smallest_number)



# print (k)

#
# min = k[0]
# max = k[0]
# sum = 0
# print(k)
# for i in k:
#     if i < min:
#         min = i
#     elif i>max:
#         max = i
#     sum = sum+i
#
# average = sum/len(k)
#
# print('the smallest number is ', min)
# print('the largest number is ', max)
# print('the average of all numbers is ', average)

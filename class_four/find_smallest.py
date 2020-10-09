
big_list = []

with open("temperatures.txt", "r") as fin:
    for line in fin:
        fs = line.split()
        # print (fs)
        for f in fs:
            big_list.append(int(f))

print (big_list)

smallest_number = None

#
# print  (big_list)
#
largest_number = None
visited_list = []
counter = 0

for n in big_list:
    if n in visited_list:
        print ("%s is a duplicate" % n)
    else:
        counter = counter + 1
    visited_list.append(n)

print (counter)

# largest_number = None
# total_product = 1
#
#
# # [1, 2, 3, 1, 4, 100, 80, 70, -1, -100]
# visited_list = []
# uniq_number_counter = 0
# for n in big_list:
#     if n in visited_list:
#         print ("getting duplicate %s" % n)
#     else:
#         uniq_number_counter = uniq_number_counter + 1
#     visited_list.append(n)
#
# print (uniq_number_counter)
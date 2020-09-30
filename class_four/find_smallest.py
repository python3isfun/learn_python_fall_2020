
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
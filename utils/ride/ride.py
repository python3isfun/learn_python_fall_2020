"""
ID: dayong.1
LANG: PYTHON3
TASK: ride
"""

lines = []
with open("ride.in", "r") as fin:
    for line in fin:
        lines.append(line.rstrip())
# print (lines)

first = lines[0]
second = lines[1]
print (first)
print (second)

first_product = 1
for i in first:
    print (i)
    value =  (ord(i) - 64)
    first_product = first_product * value

print (first_product)

second_product = 1
for i in second:
    print (i)
    value =  (ord(i) - 64)
    second_product = second_product * value

print (second_product)

print (first_product%47)


print (second_product%47)

fout = open("ride.out", "w")

if (first_product%47 == second_product%47):
    print ("GO")
    fout.write("GO")
else:
    print ("STAY")
    fout.write("STAY")
fout.write("\n")
fout.close()


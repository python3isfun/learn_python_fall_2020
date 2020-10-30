


############################################
# ord() and how to use it solve problem ride - train.usaco.org
############################################

fin = open ('ride.in', 'r')
fout = open("ride.out", "w")
d = fin.readlines()
first = d[0].rstrip()
second = d[1].rstrip()
# print (first)
product = 1
for p in first:
    # print (p)
    # print (ord(p) - 64)
    product = product * (ord(p) - 64)

first = product % 47


############################################
# reverse a sentence word by word
############################################

x = "apple is good"
p = x.split()
print (x)
print (p)
v = 0
new_list = []
for i in p:
    # new_list.insert(0, p[v])
    print ("current word is %s" % i)
    print ("before adding, the result is %s" % new_list)

    new_list = [p[v]] + new_list
    print ("after adding, the result is %s" % new_list)

    v = v + 1
print ("... ... reverse sentence by words using for loop")
print (new_list)



############################################
# reverse a sentence character by character
############################################

x = "apple is good"

#print ("doog si elppa")

s = ""
for i in x:
    s = i + s
print ("... ... reverse sentence using for loop")
print (s)

# using step size in python
print ("... ... reverse sentence using step syntax in list index")
print (x[::-1])
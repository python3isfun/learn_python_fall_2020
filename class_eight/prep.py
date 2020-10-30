

x = "apple is good"
p = x.split()
print (x)
print (p)
v = 0
new_list = []
for i in p:
    # new_list.insert(0, p[v])
    print ("current word is %s" % i)
    print ("before adding, the result is  word is %s" % i)

    new_list = [p[v]] + new_list
    v = v + 1
print (new_list)

# print ("good is apple")
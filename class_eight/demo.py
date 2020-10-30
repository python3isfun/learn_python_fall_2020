'''
reverse a sentence reviewed

reverse a string

shift a string

'''

ord()


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
print (new_list)

# print ("good is apple")





x = "apple is good"

print ("doog si elppa")

s = ""
for i in x:
    s = i + s
print (s)

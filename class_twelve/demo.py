
d = {1:2, 3:4}

d = {'Helena': 15, 'Olivia': 25, 'Brandon': 55, 'Vincent': 38, 'Aidan': 27, "Aaron":10,  1:2}

print (d)

print (d['Helena'])

d ['Helena'] = d["Helena"] + 5

print (d['Helena'])
print (d)

#
# students = ["Helena", "Alex", "Brandon", "Olivia"]
# for v in students:
#     print (v)

# for k, v in d.items():
#     print ("student named " + k + " has this much money: ", v + 5)
#     d[k] = v + 5
# print (d)
#
# # print (len(d))
#
# print (d['Helena'])
#
# # iterate through dictionary
# for k, v in d.items():
#     print (k, v)
#
# for x in d.items():
#     print (x)
#     k, v = x
#     print (k, v)

for k, v in d.items():
    d[k] = v + 5
print (d)

d["Alex"] = 100
print (d)